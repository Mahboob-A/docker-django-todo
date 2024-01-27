from django.db import models

# Create your models here.

class TodoData(models.Model): 
        headline = models.CharField(max_length=100, help_text='Headline of Your Task')
        text = models.CharField(max_length=500, help_text='Descriptioni of Your Task')
        status = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        
        def __str__(self) -> str:
                return self.headline
        
        
        


