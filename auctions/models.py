from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


# class Listing(models.Model):
#     title= models.CharField(max_length = 64)
#     description = models.CharField(max_length=1000)
#     bid = models.IntegerField()
#     image = models.ImageField(upload_to="Images")

#     def __str__(self):
#         return f"{self.title}"

# class WatchList(models.Model):
#     item = models.ManyToManyField(Listing, blank=True, related_name="watchlist")
    