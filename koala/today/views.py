from django import http
from django.http.response import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    return HttpResponse("Enter your login details here")

def view_account_details(request):
    return HttpResponse("View your account details here")

def logout(request):
    return HttpResponse("Logged out successfully. Goodbye")    