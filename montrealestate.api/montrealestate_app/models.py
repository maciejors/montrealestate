from django.db import models


class Apartment(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    longDescription = models.TextField(default='')
    price = models.FloatField(default=0)
    category = models.CharField(max_length=255)
    constructionYear = models.IntegerField(default=0)
    walkScore = models.IntegerField(default=0)
    noRooms = models.IntegerField(default=0)
    noBedrooms = models.IntegerField(default=0)
    noFireplaces = models.IntegerField(default=0)
    noGarages = models.IntegerField(default=0)
    noParkingLots = models.IntegerField(default=0)
    noPools = models.IntegerField(default=0)
    photoUrl = models.CharField(max_length=255)
    isNew = models.BooleanField(default=True)
    googleMapAddressLink = models.CharField(max_length=255)
    walkScoreMapped = models.CharField(max_length=255)
    livingArea = models.FloatField(default=0)
    contactEmail = models.CharField(max_length=255)
    contactPhoneNumber = models.CharField(max_length=255)
    noBathrooms = models.IntegerField(default=0)

    def __str__(self):
        return self.address
