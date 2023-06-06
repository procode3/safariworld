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

def index(request):
    adventures = Adventure.objects.order_by('departure_date')[:4]
    context = {"adventures": adventures}
    return render(request, 'booking/index.html', context)

def adventures(request):
    p = Paginator(Adventure.objects.all(), 3)
    page = request.GET.get('page')
    adventures = p.get_page(page)
    context = {"adventures": adventures}
    return render(request, 'booking/all_adventures.html', context)

def adv_details(request, id):
    adventure_url = reverse('adventure', args=[id])
    adv = Adventure.objects.get(id=id)
    activities = [activity.strip() for activity in adv.activities.split(",")]

    p = Paginator(adv.itinerary_advs.all(), 3)
    page = request.GET.get('page')
    itineraries = p.get_page(page)
    context = {'adventure_url': adventure_url, 'adv': adv, 'activities': activities, 'itineraries': itineraries }

    return render(request, 'booking/adventure.html', context)

def book_adv(request, id):
    authenticated = True

    if authenticated:
        return redirect(f'/{id}/order')
    else:
        return redirect('/login')

@login_required
def order_page(request, id):
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
        
        
    adventure = Adventure.objects.get(id=id)
    context = {'adventure': adventure}

    return render(request, 'booking/order.html', context) 

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')

        user = authenticate(request, username=username, password=password)
        next = request.POST.get('next', '/')
        if user is not None:
            login(request, user)

            if remember_me:
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            return HttpResponseRedirect(next)

    return render(request, 'booking/login.html')

def logout_page(request):
    next = request.GET.get('next', '/')
    logout(request)
    pattern = r'/.*/order'
    if re.match(pattern, next):
        next = '/'
    return HttpResponseRedirect(next)

def signup_page(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print('Error submitting')
    context = {
                'form': form,
            }
    return render(request, 'booking/signup.html', context)      
