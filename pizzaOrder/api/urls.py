from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.urls import path

urlpatterns = [   
    path('ingredients/get/', views.IngredientsView.as_view()),    
    path('pizza/get/', views.PizzaView.as_view()),
    path('client/post/', views.ClientView.as_view()),
    path('client/get/<str:client_id>', views.ClientView.as_view()),
    path('order/getall/', views.OrderView.as_view()),
    path('order/get/<int:order_id>', views.OrderGetView.as_view()),
    path('order/post/', views.OrderView.as_view()),
    path('bestclient/get/', views.BestIngredientsView.as_view()),
]
