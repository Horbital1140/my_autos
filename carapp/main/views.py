from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *
from django.contrib.auth import logout, login, authenticate
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ContactForm, Customer_registrationForm



# Create your views here.




def home(request):
    info = AppInfo.objects.get(pk=2)
    cat = Category.objects.all()

    context = {
        'info':info,
        'cat':cat
    }
    
    return render(request, "index.html",  context)


def landing_page(request):
    info = AppInfo.objects.get(pk=2)

    context = {
        'info':info,
        
    }
    return render (request, 'landingpage.html', context)


                  

def product(request):
    car_product = Product.objects.all()
    info = AppInfo.objects.get(pk=2)

    context = {
        'car_product':car_product,
        'info':info,

    }
    return render(request, "product.html", context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your messages has been sent successfully')
            return redirect('home')

    info = AppInfo.objects.get(pk=2)    
    context = {
            'form': form,
            'info':info,
        }
        

    return render(request, 'contact.html', context)




def signout(request):
    logout(request)
    messages.success(request, 'Dear client, you have sign out successfully')
    return redirect('signin')

    


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Dear Client, you have successfully login')
            return redirect('home')
        else:
            messages.error(request, 'username/password is incorrect, please enter correct login details')
            return redirect('signin')
        
    info = AppInfo.objects.get(pk=2)    
    context = {
            
            'info':info,
        }
        
    return render(request, 'login.html', context)



def register(request):
    register = Customer_registrationForm()
    if request.method == 'POST':
        # calling out the label in our model thatnis not in django register form creation
        username = request.POST['username']
        city = request.POST['city']
        phone_number = request.POST['phone_number']
        profile_picture =  request.POST['profile_picture']
        #calling out stop
        
        register = Customer_registrationForm(request.POST)
        if register.is_valid():
            user = register.save()
            newuser = Customer_registration(user=user)
            newuser.first_name = user.first_name
            newuser.last_name = user.last_name
            newuser.email = user.email
            newuser.phone_number = phone_number
            newuser.username = username
            newuser.city = city
            newuser.profile_picture = profile_picture
            newuser.save()
            messages.success(request, f'dear {user.username} your account has been created succesfully')
            return redirect('signin')
        else:
            messages.error(request, register.errors)

    info = AppInfo.objects.get(pk=2)    
    context = {
            
            'info':info,
        }
        

          
    return render(request, 'register.html', context)

