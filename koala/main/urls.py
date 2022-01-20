from django.urls import path
from .views import home_page, contact_us, about_us

urlpatterns = [
    path('', home_page, name ='home'),
    path("contact/", contact_us, name= 'contact'),
    path("about/", about_us, name= 'about')
   ]
