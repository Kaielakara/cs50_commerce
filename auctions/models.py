from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Listing(models.Model):
    choice_category = [
        ("AN", "Anime"),
        ("CR", "Cars"),
        ("NA", "Nature"),
        ("SP", "Self Portrait")
    ]

    title = models.CharField(max_length = 64)
    description = models.CharField(max_length=1000)
    category = models.CharField(choices = choice_category, max_length = 50)
    bid = models.IntegerField()
    user = models.CharField(max_length = 64)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return f"{self.title}"

class WatchList(models.Model):
    item = models.ForeignKey(Listing, on_delete = models.CASCADE , related_name="watchlist")
    person = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "person")

    def __str__(self):
        return f"{self.item}"
    