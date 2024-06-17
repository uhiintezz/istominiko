from django.db import models

# Create your models here.



class Contact(models.Model):
    '''Класс контактов'''

    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=14)
    message = models.TextField(max_length=1200)
    created_at = models.DateTimeField(auto_now_add=True)
