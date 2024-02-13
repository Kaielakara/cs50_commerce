from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *

from .models import *


def index(request):
    listing = Listing.objects.filter(active = False)
    return render(request, "auctions/index.html", {
        "listing" : listing
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create(request):
    # Once a request comes in with a post method
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        # you validate the form
        if form.is_valid():
            form.save()
            return create_error(request, "Successfully filled data")

        else:
            return create_error(request, "Unsucessful")          

    else:
        return render(request, "auctions/create.html", {
            "form" : UploadForm(),
        })
   
    
@login_required   
def watchlist(request):
    # once it is accessed view the post method alongside certain details
    # you get the particular Listing object and save that object as a new Watchlist
    # you are also redirected to your index page 
    if request.method == "POST":
        id = request.POST["list_data"]
        user_data = request.POST["user_data"]
        wl = Listing.objects.get(pk = id)
        user_obj = User.objects.get(pk = user_data)
        new = WatchList(item = wl, person = user_obj)
        new.save()
        return HttpResponseRedirect(reverse("auctions:index"))
    
    # if it is accessed through get you create an empty list and you also try to query the entire model
    # You then loop through each object of the Wachlist filtering each Listing to find out which has a
    # title like the current index, and then you append the first index of the queryset and you display the list 
    else:
        new_watchlist = []
        wl = WatchList.objects.filter(person = request.user.pk)
        for i in wl:
            new_w = Listing.objects.filter(title = i)
            new_watchlist.append(new_w[0])

        return render(request, "auctions/watchlist.html", {
            "watchlist" : new_watchlist
        })

@login_required   
def remove_watchlist(request):
    if request.method == "POST":
        new_id = request.POST['list_data']
        list = Listing.objects.get(pk = new_id)
        wl = WatchList.objects.get(item = list).delete()
        return HttpResponseRedirect(reverse("auctions:watchlist"))


@login_required
def product(request, name):
    list = Listing.objects.get(title = name)
    form = BidForm()
    return render(request, "auctions/product.html", {
        "list" : list,
        "form" : form
    })


@login_required
def product_bid(request):
    if request.method == "POST":
        bid = request.POST['bid']
        list_id = request.POST['list_data']
        list_user = request.POST['list_user']
        list = Listing.objects.get(pk = list_id)
        if list.bid >= int(bid):
            return HttpResponseRedirect(reverse("auctions:product", args = [list.title]))
        else:
            list.bid = bid
            list.bidder = list_user
            list.save()
            return render(request, "auctions/product.html", {
                "message" : "Successfully placed a Bid"
            })
        

@login_required
def product_close(request):
    if request.method == "POST":
        list_id = request.POST['list_data']
        list = Listing.objects.get(pk = list_id)
        list.active = True
        list.save()
        return render(request, "auctions/product.html", {
            "message" : "Successfully Closed the Bid"
        })
    
def create_error(request, str):
    return render(request, "auctions/create.html", {
        "form" : UploadForm(),
        "message" : str
    })