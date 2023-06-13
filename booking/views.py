from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from .models import Adventure, Booking, User
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import re
from django.conf import settings
import json
import requests


def index(request):
    """Handles the index page"""
    adventures = Adventure.objects.order_by('departure_date')[:4]
    context = {"adventures": adventures}
    return render(request, 'booking/index.html', context)

def adventures(request):
    """Route for all adventures in the system"""
    p = Paginator(Adventure.objects.all(), 3)
    page = request.GET.get('page')
    adventures = p.get_page(page)
    context = {"adventures": adventures}
    return render(request, 'booking/all_adventures.html', context)

def adv_details(request, id):
    """Route for a specific adventure"""
    adventure_url = reverse('adventure', args=[id])
    adv = Adventure.objects.get(id=id)
    activities = [activity.strip() for activity in adv.activities.split(",")]

    p = Paginator(adv.itinerary_advs.all(), 3)
    page = request.GET.get('page')
    itineraries = p.get_page(page)
    context = {'adventure_url': adventure_url, 'adv': adv, 'activities': activities, 'itineraries': itineraries }

    return render(request, 'booking/adventure.html', context)

@login_required
def order_page(request, id):
    """Handles booking for a specific adventure"""
    print(f'user in both methods: {request.user}')
    adventure = Adventure.objects.get(id=id)
    if request.method == 'POST':
        obj = json.loads(request.body)
        slots = adventure.slots
        remaining_slots = slots - int(obj.get('count'))
        adventure.slots = remaining_slots
        print(f'User in POST: {request.user.id}')
        adventure.save()
        user = User.objects.get(id=request.user.id)
        booking_kwargs = {
            'user_id': user,
            'adventure_id': adventure,
            'number_of_persons': int(obj.get('count')),
            'amount_paid': adventure.price*int(obj.get('count')),
            'is_confirmed': True
            }
        booking = Booking(**booking_kwargs)
        booking.save()
        
        url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        headers = {
                 'Content-Type': 'application/json',
                 'Authorization': 'Basic Rm90cDJBdjdrUDl1djc5TTNZdUc3SHhId0padkRaNEc6STF5MmVGT0RnY1N2azFncA',            
                 }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(data)
            prompt_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {
                      'Content-Type': 'application/json',
                      'Authorization': f'Bearer {data.get("access_token")}',           
                      }
            
            body =   {
                  "BusinessShortCode": 174379,
                  "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMwNjAzMDAyOTE3",
                  "Timestamp": "20230603002917",
                  "TransactionType": "CustomerPayBillOnline",
                  "Amount": 5,
                  "PartyA": 254708374149,
                  "PartyB": 174379,
                  "PhoneNumber": f'254{obj.get("phone")}',
                  "CallBackURL": "https://mydomain.com/path",
                  "AccountReference": "Samburu Glamping",
                  "TransactionDesc": "Payment of X" 
                  }
            response = requests.post(prompt_url, data=json.dumps(body), headers=headers)
            if response.status_code == 200:
                print('Sucessful')
            else:
                print('Try again')
            
        else:
            print('An error occurred:', response.status_code)
    adventure = Adventure.objects.get(id=id)
    context = {'adventure': adventure}

    return render(request, 'booking/order.html', context) 

def login_page(request):
    """Handles user authentication"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')

        user = authenticate(request, username=username, password=password)
        next = request.POST.get('next', '/')
        if not next:
            next='/'
        if user is not None:
            login(request, user)

            if remember_me:
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            return HttpResponseRedirect(next)

    return render(request, 'booking/login.html')

def logout_page(request):
    """Ends the current user session"""
    next = request.GET.get('next', '/')
    logout(request)
    pattern = r'/.*/order'
    if re.match(pattern, next):
        next = '/'
    return HttpResponseRedirect(next)

def signup_page(request):
    """Handles the creation of a user"""
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print('Error submitting')
            print(form.errors)
    context = {
                'form': form,
            }
    return render(request, 'booking/signup.html', context)
