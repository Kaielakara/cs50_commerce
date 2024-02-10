from django.urls import path

from . import views

app_name = "auctions"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("remove/watchlist", views.remove_watchlist, name='remove_watchlist' ),
    path("product", views.product_bid, name="product_bid"),
    path("product/placebid", views.place_bid, name="place_bid")
]
