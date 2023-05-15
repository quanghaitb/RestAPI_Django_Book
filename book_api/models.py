from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    number_of_pages = models.CharField(max_length=50)
    publish_date = models.DateField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.title