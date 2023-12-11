from django.urls import path
from main import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home', views.home, name='home'),
    path('product', views.product, name='product'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('landing_page', views.landing_page, name='landing_page'),
    
]