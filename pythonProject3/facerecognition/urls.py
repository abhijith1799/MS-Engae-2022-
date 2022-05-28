from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.listing, name = "listing"),
    path("categories", views.categories, name="categories"),
    path("listing/<str:category>", views.list_categories, name="list_categories"),
    path("create", views.create, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("toggle_watchlist/<int:listing_id>", views.toggle_watchlist, name = "toggle_watchlist"),
     path("close/<int:listing_id>", views.close, name = "close")
]
