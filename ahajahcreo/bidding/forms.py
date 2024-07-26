
from django import forms
from .models import Auction
from .models import Bid

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['title', 'description', 'starting_bid', 'ends_at']


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_amount']

