from rest_framework import serializers
from .models import Client, Ingredients, Order, Pizza


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('client_id', 'client_name', 'address', 'phone')


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = ('ingredient_id', 'ingredient_name', 'ingredient_price')


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = ('pizza_id', 'pizza_size', 'price')


class OrderSerializer(serializers.ModelSerializer):

    order_total = serializers.ReadOnlyField()
    ingredients_arr = serializers.ReadOnlyField()

    class Meta:
        model = Order
        depth = 2
        fields = ('order_id', 'client', 'pizza', 'ingredients', 'order_total',
                  'ingredients_arr')


class OrderPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('client', 'pizza', 'ingredients')


