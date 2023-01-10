from rest_framework import serializers
from .models import Apartment


class ListingFull(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ["id",
                  "photoUrl",
                  "price",
                  "livingArea",
                  "constructionYear",
                  "city",
                  "district",
                  "address",
                  "categories",
                  "noRooms",
                  "noBedrooms",
                  "noBathrooms",
                  "noGarages",
                  "noParkingLots",
                  "isNew",
                  "googleMapsAddressLink",
                  "walkScore",
                  "walkScoreMapped",
                  "longDescription",
                  "contactEmail",
                  "contactPhoneNumber"]


class ItemsSerializer(serializers.Serializer):
    items = serializers.ListField()
