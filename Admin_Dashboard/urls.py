from django.contrib import admin
from django.urls import path, include
from . import views
# from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.orders, name="AdminHome"),

    path('customers/', views.customers, name="Customer"),
    path('subscribers/', views.subscribers, name="Subscribers"),
    path('queries/', views.queries, name="Query"),
    path('upload/', views.upload, name="Upload"),
    path('viewImage<str:name>/', views.viewImage, name="ViewImage"),
    path('addNewImage/<str:name>/<str:plan>', views.addNewImage, name="AddNewImage"),
    path('orderForMeals/', views.orderForMeals, name="OrderForMeals"),
    path('orderForTrans/', views.orderForTrans, name="OrderForTrans"),
    path('orderTransEdit/<str:orderId>', views.orderTransEdit, name="OrderTransEdit"),
    path('orderMealsEdit/<str:orderId>', views.orderMealsEdit, name="OrderMealsEdit"),

]
