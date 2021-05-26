"""Nutricraftors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
urlpatterns = [
    path('admin_dashboard/', include('Admin_Dashboard.urls')),
    path('', views.home, name="Home"),
    path('admin/', admin.site.urls),
    path('login/', views.login, name="Login"),
    path('register/', views.register, name="Register"),
    path('forgot/', views.forgot, name="Forgot"),
    path('logout/', views.logout, name="Logout"),
    path('contactUs/', views.contactUs, name="Contact"),
    path('meals/', views.meals, name="Meals"),
    path('choosePlans/', views.choosePlans, name="ChoosePlans"),

    path('mealbox/', views.mealbox, name="Mealbox"),
    path('transformation/', views.transformation, name="Transformation"),
    # path('update_profile/<str:uid>/', views.updateProfile, name="updateProfile"),

    path('mealbox-know-more/<str:name>/',
         views.mealboxKnowMore, name="MealboxKnowMore"),
    path('transformationKnowMore/<str:name>/',
         views.transformationKnowMore, name="TransformationKnowMore"),
    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name='forgot-password.html'), name="PasswordReset"),
    # path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
    #     template_name='password_reset_done.html'), name="password_reset_done"),
    # path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
    #     template_name='reset.html'), name="password_reset_confirm"),
    # path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(
    #     template_name='password_reset_complete.html'), name="password_reset_complete"),

    path('subscribe/', views.subscribe, name="Subscribe"),
    path('aboutUs/', views.aboutUs, name="AboutUs"),
    path('OrderTransformationPlan/', views.OrderTransformationPlanDef,
         name="OrderTransformationPlan"),

    path('OrderMealPlan/', views.OrderMealPlan,
    name="OrderMealPlan"), 
    path('checkout/', views.checkout, name="Checkout"),
    path('checkOutForMeal/', views.checkOutForMeal, name="CheckOutForMeal"),
    path('myOrders/', views.myOrders, name="MyOrders"),
    path('orderForMealsUser/', views.orderForMealsUser, name="OrderForMealsUser"),
    path('orderForTransUser/', views.orderForTransUser, name="OrderForTransUser"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
