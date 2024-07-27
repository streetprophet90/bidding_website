from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Auction, Bid
from .forms import AuctionForm, BidForm


# Home view
def home(request):
    return render(request, 'bidding/home.html')

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'bidding/register.html', {'form': form})

# Index view for listing all auctions
def index(request):
    auctions = Auction.objects.all()
    return render(request, 'bidding/index.html', {'auctions': auctions})

# Detailed view for a single auction
def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.auction = auction
            bid.bidder = request.user
            if auction.current_bid is None or bid.bid_amount > auction.current_bid:
                auction.current_bid = bid.bid_amount
                auction.save()
                bid.save()
            return redirect('auction_detail', auction_id=auction.id)
    else:
        form = BidForm()
    return render(request, 'bidding/auction_detail.html', {'auction': auction, 'form': form})

# View for creating a new auction
@login_required
def create_auction(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.creator = request.user
            auction.save()
            return redirect('index')
    else:
        form = AuctionForm()
    return render(request, 'bidding/create_auction.html', {'form': form})
