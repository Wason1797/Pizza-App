from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClientSerializer,\
                         PizzaSerializer, IngredientsSerializer,\
                         OrderSerializer, OrderPostSerializer
from .models import Client, Ingredients, Order, Pizza


# Create your views here.
class IngredientsView(APIView):

    def get(self, request):
        queryset = Ingredients.objects.all()
        serializer = IngredientsSerializer(queryset, many=True)
        return Response(serializer.data)


class PizzaView(APIView):

    def get(self, request):
        queryset = Pizza.objects.all()
        serializer = PizzaSerializer(queryset, many=True)
        return Response(serializer.data)


class ClientView(APIView):

    def get(self, request, client_id):
        queryset = Client.objects.get(client_id=client_id)
        serializer = ClientSerializer(queryset)
        return Response(serializer.data)

    def post(request, format=None):

        serializer = ClientSerializer(data=request.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "client created succesfully"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)


class OrderGetView(APIView):

    def get(self, request, order_id):
        queryset = Order.objects.get(order_id=order_id)
        serializer = OrderSerializer(queryset)
        return Response(serializer.data)


class OrderView(APIView):

    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(request, format=None):

        serializer = OrderPostSerializer(data=request.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "order created succesfully"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)
