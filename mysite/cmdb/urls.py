from django.urls import path
from . import views

app_name = 'cmdb'

urlpatterns = [
    path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('detail/<int:asset_id>/', views.detail, name="detail"),
    path('', views.dashboard),
]
