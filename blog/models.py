from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32)
    
    
    class meta:
        verbos_name_prulal = "users"
        
        
    def __str__(self):
        return self.username
        