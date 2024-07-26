
from django.shortcuts import render, get_object_or_404
from .models import Auction

def index(request):
    auctions = Auction.objects.all()
    return render(request, 'bidding/index.html', {'auctions': auctions})

def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    return render(request, 'bidding/auction_detail.html', {'auction': auction})

def home(request):
    return render(request, 'bidding/home.html')
