from django.urls import path
from . import views
from django.urls import include
app_name = 'login'

urlpatterns = [

    path('', views.login, name='login'),
    path('index', views.index),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('confirm/', views.user_confirm)
]
