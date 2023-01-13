import sys

import rest_framework.request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Apartment
from .serializers import ListingFull, ItemsSerializer
import sqlite3
from sqlite3 import Error


class ApiCitiesView(APIView):

    def get(self, *args, **kwargs):
        """
        List all distinct cities
        """
        connection = sqlite3.connect("db.sqlite3")
        query = "SELECT DISTINCT CITY FROM MONTREALESTATE_APP_APARTMENT"
        cursor = connection.cursor()
        cursor.execute(query)
        query_result = cursor.fetchall()
        result = []
        for elem in query_result:
            result.append(elem[0])
        print(result)
        serializer = ItemsSerializer(data={'items': result})
        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiDistrictsView(APIView):

    def get(self, city, *args, **kwargs):
        """
        List all districts in a given city
        """
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT DISTRICT FROM MONTREALESTATE_APP_APARTMENT WHERE CITY = ?",
                       [city.GET['city']])
        query_result = cursor.fetchall()
        result = []
        for elem in query_result:
            result.append(elem[0])
        print(result)
        serializer = ItemsSerializer(data={'items': result})
        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiCategoriesView(APIView):

    def get(self, *args, **kwargs):
        """
        List all categories
        """
        result = ['Apartment',
                  'Commercial',
                  'Detached',
                  'Duplex',
                  'House',
                  'LoftStudio',
                  'Multiplex',
                  'Other',
                  'Quadruplex',
                  'Triplex']
        serializer = ItemsSerializer(data={'items': result})
        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiListings(APIView):

    def get(self,
            startFrom=1,
            no_records=1,
            city='.*',
            district='.*',
            minPrice=0,
            maxPrice=sys.maxsize,
            minFloorArea=0,
            maxFloorArea=sys.maxsize,
            minConstructionYear=0,
            maxConstructionYear=sys.maxsize,
            minRooms=0,
            maxRooms=sys.maxsize,
            minBedrooms=0,
            maxBedrooms=sys.maxsize,
            minBathrooms=0,
            maxBathrooms=sys.maxsize,
            minGarages=0,
            maxGarages=sys.maxsize,
            minParkingLots=0,
            maxParkingLots=sys.maxsize,
            onlyNew=False,
            walkScoreThreshold=0,
            apartment=0,
            commercial=0,
            detached=0,
            house=0,
            loftStudio=0,
            multiplex=0,
            other=0,
            quadruplex=0,
            triplex=0,
            *args, **kwargs):
        """
        List all distinct walkScoreMapped values
        """
        connection = sqlite3.connect("db.sqlite3")
        query = "select id, " \
                "photoUrl, " \
                "price, " \
                "livingArea, " \
                "constructionYear, " \
                "city, " \
                "district, " \
                "address," \
                "category," \
                "noRooms," \
                "isNew" \
                "from montrealestate_app_apartment" \
                "where city regexp '^' || ? || '$'" \
                "and district regexp '^' || ? || '$'" \
                "and price >= ?" \
                "and price <= ?" \
                "and livingArea >= ?" \
                "and livingArea <= ?" \
                "and constructionYear >= ?" \
                "and constructionYear <= ?" \
                "and noRooms >= ?" \
                "and noRooms <= ?" \
                "and noBedrooms >= ?" \
                "and noBedrooms <= ?" \
                "and noBathrooms >= ?" \
                "and noBathrooms <= ?" \
                "and noGarages >= ?" \
                "and noGarages <= ?" \
                "and noParkingLots >= ?" \
                "and noParkingLots <= ?" \
                "and isNew = ?" \
                "and walkScore >= ?" \
                "and apartment = ?" \
                "and commercial = ?" \
                "and detached = ?" \
                "and duplex = ?" \
                "and house = ?" \
                "and loftStudio = ?" \
                "and multiplex = ?" \
                "and other = ?" \
                "and quadruplex = ?" \
                "and triplex = ?" \
                "order by id" \
                "limit ? offset ?"
        cursor = connection.cursor()
        print(type(startFrom))
        print(type(no_records))
        print(type(city))
        city = '.*' if type(city) is str else city.GET.get('city')
        district = '.*' if type(district) is str else district.GET['district']
        print(city)
        args = (city,
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
                apartment,
                commercial,
                detached,
                house,
                loftStudio,
                multiplex,
                other,
                quadruplex,
                triplex,
                no_records,
                startFrom,)
        cursor.execute(query, args)
        query_result = cursor.fetchall()
        result = []
        for elem in query_result:
            result.append(elem[0])
        print(result)
        serializer = ItemsSerializer(data={'items': result})
        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
