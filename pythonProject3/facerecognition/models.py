from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator

class User(AbstractUser):
    id = models.IntegerField(primary_key=True)
    password =  models.CharField(max_length = 128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField(default = False)
    username = models.CharField(max_length = 150)
    email = models.CharField(max_length = 255)

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "owner")
    title = models.CharField(max_length = 64)
    description = models.TextField(blank = True)
    active = models.BooleanField(blank = False, default = True)
    img_url = models.URLField(blank = True)
    category = models.CharField(blank = True, max_length = 64)
    base_bid = models.FloatField(validators = [MinValueValidator(1)], default = 1)
    winner = models.ForeignKey(User, blank = True, on_delete = models.CASCADE, related_name = "new_owner", null = True)

    def __str__(self):
        return(f"{self.title} - {self.description} \t Starting Bid = {self.base_bid} ")

class Bids(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)
    price = models.FloatField(validators = [MinValueValidator(1)], default = 1)
    winner = models.BooleanField(default = False)

    def __str__(self):
        return(f"{self.user} bid for the item {self.listing} for a price of $ {self.price}")

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing,  on_delete = models.CASCADE)
    contents = models.TextField()

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE, blank = False)