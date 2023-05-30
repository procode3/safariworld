from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'booking/index.html')

def adventures(request):
   
    return render(request, 'booking/all_adventures.html')

def adv_details(request, id):
  return render(request, 'booking/adventure.html')

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