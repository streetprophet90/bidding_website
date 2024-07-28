
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Auction, Bid, Profile
from .forms import AuctionForm, BidForm, ProfileForm


# Home view
def home(request):
    return render(request, 'bidding/home.html')


# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Ensure profile creation only if it does not exist
            Profile.objects.get_or_create(user=user)
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserCreationForm()
    return render(request, 'bidding/register.html', {'form': form})


# Profile view
@login_required
def profile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'bidding/profile.html', {'form': form})


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
            messages.success(request, 'Auction created successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AuctionForm()
    return render(request, 'bidding/create_auction.html', {'form': form})


# Signals for creating and saving user profiles
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
