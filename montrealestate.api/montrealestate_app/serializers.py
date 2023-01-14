from rest_framework import serializers
from .models import Apartment


class ListingFull(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['id',
                  'city',
                  'photoUrl',
                  'price',
                  'livingArea',
                  'constructionYear',
                  'district',
                  'address',
                  'noRooms',
                  'noBedrooms',
                  'noBathrooms',
                  'noGarages',
                  'noParkingLots',
                  'isNew',
                  'googleMapAddressLink',
                  'walkScore',
                  'walkScoreMapped',
                  'longDescription',
                  'contactEmail',
                  'contactPhoneNumber']


class ItemsSerializer(serializers.Serializer):
    items = serializers.ListField()


class ApartmentsCountSerializer(serializers.Serializer):
    listings = serializers.ListField()
    totalCount = serializers.IntegerField()
