from django.http.response import HttpResponse
from django.shortcuts import render
from main.models import Registered_Users


# Create your views here.

def home_page(request):
    return render(request,"home.html")


# with open("main/users.txt", 'r') as file:
#     doc = file.read()
#     total_dict = eval(doc)



# def contact_us(request):
#     global total_dict
#     info = list(range(len(total_dict)+1))
#     if request.method == "POST":
#         my_dict = {}
#         my_dict['name'] = str.join('', (request.POST)['my_name'])
#         my_dict['email'] = str.join('', (request.POST)['my_email'])
#         my_dict['message'] = str.join('', (request.POST)['my_message'])
#         for i in info:
#             if i not in total_dict.keys():
#                 total_dict[i] = my_dict    
#                 break  
               

#     with open("main/users.txt",'w') as file:
#         file.write(f"{total_dict}")
#     return render(request, "contact.html")


def contact_us(request):
    if request.method == "POST":
        request_data = dict(request.POST)
        request_data.pop('csrfmiddlewaretoken')
        data = {key:request_data.get(key)[0] for key in request_data}
        Registered_Users.objects.create(user_name = data['my_name'], user_email = data['my_email'], user_message = data['my_message'])

    return render(request, "contact.html")

def about_us(request):
    return render(request, "about.html")    