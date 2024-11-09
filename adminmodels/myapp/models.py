from django.db import models

#models go here
class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=100, null=True)
    publish_date = models.DateField()

    def __str__(self):
        return f"{self.title}"
    
    