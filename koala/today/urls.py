from django.urls import path

from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login, name='login'),
    path('account/',view_account_details, name='account'),
    path('logout/',logout, name='logout'),
]