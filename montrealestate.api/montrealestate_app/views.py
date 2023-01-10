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
        # query_result = execute_read_query(connection, query)
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
                       [city.GET.dict()['city']])
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
