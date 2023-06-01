from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from .models import Adventure
from django.urls import reverse


def index(request):
    adventures = Adventure.objects.order_by('departure_date')[:4]
    context = {"adventures": adventures}
    return render(request, 'booking/index.html', context)

def adventures(request):
    adventures = Adventure.objects.all()
    context = {"adventures": adventures}
    return render(request, 'booking/all_adventures.html', context)

def adv_details(request, id):
  adventure_url = reverse('adventure', args=[id])
  adv = Adventure.objects.get(id=id)
  activities = [activity.strip() for activity in adv.activities.split(",")]
  itineraries = adv.itinerary_advs.all()[:3]
  print(itineraries[0].image)
  context = {'adventure_url': adventure_url, 'adv': adv, 'activities': activities, 'itineraries': itineraries }

  return render(request, 'booking/adventure.html', context)

def book_adv(request, id):
    authenticated = True

    if authenticated:
        return redirect(f'/{id}/order')
    else:
        return redirect('/login')

def order_page(request, id):
    return render(request, 'booking/order.html') 

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        next = request.POST.get('next', '/')
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)

    print('Error login')
    return render(request, 'booking/login.html')

def logout_page(request):
    next = request.GET.get('next', '/')
    logout(request)
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
                'form': form
            }
    return render(request, 'booking/signup.html', context)      