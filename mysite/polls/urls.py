# -*- coding: utf-8 -*-
from django.urls import path
from . import views,search,search2

app_name = 'polls'
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('<int:question_id>/', views.detail, name='detail'),
#    path('<int:question_id>/results/', views.results, name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),
#
#]
urlpatterns = [
    path('', views.IndexView.as_view(), {'name':'index'}),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('datetime/', views.current_datetime),
    path('search-form/', search.search_from),
    path('search/', search.search),
    path('search-post/', search2.search_post),
]
