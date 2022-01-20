from django.test import TestCase
from django.urls import reverse, resolve
from .views import *


# Create your tests here.
class MytestCase(TestCase):
    def test_login_view(self):
        res = resolve(reverse('login'))
        response = self.client.get(reverse('login'))
        self.assertEqual(response.content,b'Enter your login details here')
        self.assertEqual(response.status_code,200)
        self.assertEqual(res.func,login)
        self.assertEqual(reverse('login'),'/login/')
    
    def test_view_account_details_view(self):
        res = resolve(reverse('account'))    
        response = self.client.get(reverse('account'))
        self.assertEqual(response.content,b'View your account details here')
        self.assertEqual(response.status_code,200)
        self.assertEqual(res.func,view_account_details)
        self.assertEqual(reverse('account'),'/account/')

    def test_logout_view(self):
        res = resolve(reverse('logout'))    
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.content, b'Logged out successfully. Goodbye')
        self.assertEqual(response.status_code,200)
        self.assertEqual(res.func,logout)
        self.assertEqual(reverse('logout'),'/logout/')