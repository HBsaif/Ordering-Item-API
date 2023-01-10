from django.db import models

# Create your models here.

class Item(models.Model):
    ItemId = models.IntegerField(primary_key = True)
    ItemName = models.CharField(max_length=200)
    Quantity = models.IntegerField()
    Cat = models.CharField(max_length=200)
    Charity = models.CharField(max_length=200, default=None)

    def __str__ (self):
        return self.ItemName

class CharityRegistration(models.Model):
    #CharityId = models.IntegerField(primary_key = True)
    Email = models.EmailField()
    CharityName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    City = models.CharField(max_length=200)

    def __str__(self):
        return self.CharityName

class UserRegistration(models.Model):
    Email = models.EmailField()
    Username = models.CharField(max_length=200)
    CharityName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    City = models.CharField(max_length=200)

    def __str__(self):
        return self.Username

class OrderItem(models.Model):
    ItemId = models.ForeignKey('Item', on_delete=models.CASCADE)
    OrderDate = models.DateTimeField(auto_now_add=True, blank=True)
    ItemName = models.CharField(max_length=200)
    Quantity = models.IntegerField()
    Username = models.EmailField()

    def __str__(self):
        return self.Username