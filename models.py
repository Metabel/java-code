from django.db import models

class Contact(models.Model):
    name =models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return f"Name:{self.name} email:{self.email} message:{self.message}"

# Create your models here.
