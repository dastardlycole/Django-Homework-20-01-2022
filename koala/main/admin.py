from django.contrib import admin
from .models import Animal, Registered_Users

# Register your models here.
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("name","dob","specie","population","is_extinct","date_created","viewing_price")
    list_filter = ("specie","dob","viewing_price")
    list_editable = ("dob","is_extinct")
    search_fields = ("name","specie")

@admin.register(Registered_Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_email','user_message')
    list_filter = ('user_name','user_email','date_created')
    list_editable = ()
    search_fields = ('user_name','user_email')
