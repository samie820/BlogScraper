from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank = True, null = True)
    
    def __str__(self):
        return self.name
        
        
        
        
class Importance(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank = True, null = True)
    
    def __str__(self):
        return self.name