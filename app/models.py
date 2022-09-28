from django.db import models
from django.urls import reverse
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('thanks')