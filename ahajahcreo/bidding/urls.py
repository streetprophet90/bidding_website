# bidding/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auction/<int:auction_id>/', views.auction_detail, name='auction_detail'),
]
