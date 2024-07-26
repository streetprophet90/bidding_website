
from django.shortcuts import render, get_object_or_404, redirect
from .models import Auction
from .forms import AuctionForm
from django.contrib.auth.decorators import login_required

def index(request):
    auctions = Auction.objects.all()
    return render(request, 'bidding/index.html', {'auctions': auctions})

def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    return render(request, 'bidding/auction_detail.html', {'auction': auction})

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

def home(request):
    return render(request, 'bidding/home.html')
