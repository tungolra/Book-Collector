from django.db import models
from django.urls import reverse
# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publish_year = models.IntegerField()

    def __str__(self):
        return f"{self.author}: {self.title} ({self.publish_year})"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
