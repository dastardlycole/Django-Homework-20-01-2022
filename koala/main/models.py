from django.db import models

# Create your models here.
class Animal(models.Model):
    SPECIE_CHOICES = (
        ('mammal','MAMMAL'),
        ('amphibian','AMPHIBIAN'),
        ('reptile','REPTILE'),
        ('pisces','PISCES'),
        ('aves','AVES'),
    )

    name = models.CharField(max_length=200,unique=True)
    desc = models.TextField()
    dob = models.DateField()
    specie = models.CharField(max_length=200,choices=SPECIE_CHOICES)
    population = models.IntegerField(default=0)
    is_extinct = models.BooleanField()
    pic_url = models.URLField()
    viewing_price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Registered_Users(models.Model):
    user_name = models.CharField(max_length=200)        
    user_email = models.EmailField()
    user_message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.user_name