import sqlite3
import sys

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Apartment, CityMap, DistrictMap
from .serializers import ItemsSerializer, ListingFull, ApartmentsCountSerializer


def isNoneNumeric(x, default, request):
    tmp = request.GET.get(x)
    return int(tmp) if tmp is not None else default


def isNoneBoolean(x, default, request):
    tmp = request.GET.get(x)
    return tmp == 'true' if tmp is not None else default


def isNoneString(x, default, request):
    tmp = request.GET.get(x)
    return tmp if tmp is not None else default


class ApiCitiesView(APIView):

    def get(self, *args, **kwargs):
        """
        List all distinct cities
        """
        connection = sqlite3.connect("db.sqlite3")
        query = "SELECT DISTINCT CITYNAME FROM MONTREALESTATE_APP_CITYMAP"
        cursor = connection.cursor()
        cursor.execute(query)
        query_result = cursor.fetchall()
        result = []
        for elem in query_result:
            result.append(elem[0])
        serializer = ItemsSerializer(data={'items': result})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiDistrictsView(APIView):

    def get(self, city, *args, **kwargs):
        """
        List all districts in a given city
        """
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        cursor.execute("select distinct districtName from montrealestate_app_apartment maa join "
                       "montrealestate_app_citymap mac on mac.cityId = maa.city_id join "
                       "montrealestate_app_districtmap mad on mad.districtId = maa.district_id "
                       "where cityName = ?",
                       [city.GET['city']])
        query_result = cursor.fetchall()
        result = []
        for elem in query_result:
            result.append(elem[0])
        serializer = ItemsSerializer(data={'items': result})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiListings(APIView):

    @staticmethod
    def get_object(startFrom,
                   count,
                   city,
                   district,
                   minPrice,
                   maxPrice,
                   minFloorArea,
                   maxFloorArea,
                   minConstructionYear,
                   maxConstructionYear,
                   minRooms,
                   maxRooms,
                   minBedrooms,
                   maxBedrooms,
                   minBathrooms,
                   maxBathrooms,
                   minGarages,
                   maxGarages,
                   minParkingLots,
                   maxParkingLots,
                   onlyNew,
                   walkScoreThreshold,
                   sortBy,
                   sortAscending):
        sortBy = sortBy if sortAscending else ('-' + sortBy)
        base_query = Apartment.objects \
            .filter(city_id__cityName__iregex='^' + city + '$') \
            .filter(district_id__districtName__iregex='^' + district + '$') \
            .filter(price__gte=minPrice) \
            .filter(price__lte=maxPrice) \
            .filter(livingArea__gte=minFloorArea) \
            .filter(livingArea__lte=maxFloorArea) \
            .filter(constructionYear__gte=minConstructionYear) \
            .filter(constructionYear__lte=maxConstructionYear) \
            .filter(noRooms__gte=minRooms) \
            .filter(noRooms__lte=maxRooms) \
            .filter(noBedrooms__gte=minBedrooms) \
            .filter(noBedrooms__lte=maxBedrooms) \
            .filter(noBathrooms__gte=minBathrooms) \
            .filter(noBathrooms__lte=maxBathrooms) \
            .filter(noGarages__gte=minGarages) \
            .filter(noGarages__lte=maxGarages) \
            .filter(noParkingLots__gte=minParkingLots) \
            .filter(noParkingLots__lte=maxParkingLots) \
            .filter(walkScore__gte=walkScoreThreshold)
        if onlyNew:
            base_query = base_query.filter(isNew=onlyNew).all()
        listings = base_query.order_by(sortBy).values()[startFrom:(startFrom + count)]
        no_listings = base_query.count()
        try:
            return listings, no_listings
        except Apartment.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        """
        List all listings matching filters
        """
        startFrom = isNoneNumeric('startFrom', 1, request)
        count = isNoneNumeric('count', 1, request)
        apartment_instance, no_records \
            = self.get_object(startFrom,
                              count,
                              isNoneString('city', '.*', request),
                              isNoneString('district', '.*', request),
                              isNoneNumeric('minPrice', 0, request),
                              isNoneNumeric('maxPrice', sys.maxsize, request),
                              isNoneNumeric('minFloorArea', 0, request),
                              isNoneNumeric('maxFloorArea', sys.maxsize, request),
                              isNoneNumeric('minConstructionYear', 0, request),
                              isNoneNumeric('maxConstructionYear', sys.maxsize, request),
                              isNoneNumeric('minRooms', 0, request),
                              isNoneNumeric('maxRooms', sys.maxsize, request),
                              isNoneNumeric('minBedrooms', 0, request),
                              isNoneNumeric('maxBedrooms', sys.maxsize, request),
                              isNoneNumeric('minBathrooms', 0, request),
                              isNoneNumeric('maxBathrooms', sys.maxsize, request),
                              isNoneNumeric('minGarages', 0, request),
                              isNoneNumeric('maxGarages', sys.maxsize, request),
                              isNoneNumeric('minParkingLots', 0, request),
                              isNoneNumeric('maxParkingLots', sys.maxsize, request),
                              isNoneBoolean('onlyNew', False, request),
                              isNoneNumeric('walkScoreThreshold', 0, request),
                              isNoneString('sortBy', 'id', request),
                              isNoneBoolean('sortAscending', True, request))
        if not apartment_instance:
            return Response(
                {"listings": [], "totalCount": 0},
                status=status.HTTP_200_OK
            )
        print(apartment_instance.values())

        result = []
        for elem in apartment_instance:
            id_city = elem['city_id']
            id_district = elem['district_id']
            elem['city'] = CityMap.objects.filter(cityId=id_city) \
                .values('cityName').get()['cityName']
            elem['district'] = DistrictMap.objects.filter(districtId=id_district) \
                .values('districtName').get()['districtName']
            result.append(elem)
        serializer = ApartmentsCountSerializer(data={'listings': result, 'totalCount': no_records})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiListingsById(APIView):

    def get_object(self, id):
        try:
            return Apartment.objects.get(id=id)
        except Apartment.DoesNotExist:
            return None

    def get(self, request, id, *args, **kwargs):
        """
        Return a listing with a specific id
        """
        apartment_instance = self.get_object(id)
        if not apartment_instance:
            return Response(
                {"listings": [], "totalCount": 0},
                status=status.HTTP_200_OK
            )
        print(apartment_instance)
        serializer = ListingFull(apartment_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
