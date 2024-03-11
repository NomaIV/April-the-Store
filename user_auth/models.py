from django.db import models

# User for online store
class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    mobile_number = models.CharField(max_length=15)
    def __str__(self):
        return self.username
    
