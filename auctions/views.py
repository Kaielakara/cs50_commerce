from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *

from .models import *


def index(request):
    listing = Listing.objects.all()
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
        return HttpResponseRedirect(reverse("auction:index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    # Once a request comes in with a post method
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        # you validate the form
        if form.is_valid():
            form.save()
            return create_error(request, "Successfully filled data")

        else:
            return create_error(request, "Unsuccessful")          

    else:
        return render(request, "auctions/create.html", {
            "form" : UploadForm(),
        })
    
    
def watchlist(request):
    if request.method == "POST":
        id = request.POST["list_data"]
        wl = Listing.objects.get(pk = id)
        new = WatchList(item = wl)
        new.save()
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        new_watchlist = []
        wl = WatchList.objects.all()
        for i in wl:
            new_w = Listing.objects.filter(title = i)
            new_watchlist.append(new_w[0])
        # return HttpResponse(watchlist)
        # new_watchlist = Listing.objects.filter(pk = watchlist.pk)
        # new_watchlist.save()

        return render(request, "auctions/watchlist.html", {
            "watchlist" : new_watchlist
        })

def create_error(request, str):
    return render(request, "auctions/create.html", {
        "form" : UploadForm(),
        "message" : str
    })