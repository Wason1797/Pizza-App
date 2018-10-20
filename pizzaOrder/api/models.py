# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create,
#  modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field 
# names.
from django.db import models
from django.contrib.postgres.fields import JSONField


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING)
    pizza = models.ForeignKey('Pizza', models.DO_NOTHING)
    ingredients = JSONField()   # This field type is a guess.

    @property
    def order_total(self):
        result = self.ingredients.replace("{", "").replace("}", "")
        result = result.split(",")
        sum_total = 0
        for item in result:
            sum_total += int(item.split("@")[1].replace("\"", ""))     
        return sum_total+self.pizza.price
    
    @property
    def ingredients_arr(self):
        result = self.ingredients.replace("{", "").replace("}", "")
        result = result.split(",")
        ing_arr = []
        for item in result:
            ing_arr.append(item.split("@")[0].replace("\"", ""))
        return ing_arr
        
    class Meta:
        managed = False
        db_table = 'ORDER'


class Client(models.Model):
    client_id = models.CharField(primary_key=True, max_length=50)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'  


class Ingredients(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)
    ingredient_name = models.CharField(max_length=50, blank=True, null=True)
    ingredient_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class Pizza(models.Model):
    pizza_id = models.IntegerField(primary_key=True)
    pizza_size = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pizza'
