from django.db import models

# Create your models here.


    

class Tweet(models.Model):
    name = models.CharField(max_length=200)
    tweets = models.TextField(blank=True, null=True)
    positive_remark = models.CharField(max_length=200, blank=True, null=True)
    negative_remark = models.CharField(max_length=200, blank=True, null=True)
    
    
    def __str__(self):
        return self.name
        
        

        
        