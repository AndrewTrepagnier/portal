""" To access the view for the portal in a browser, you need to map the view to a url.

To do this we need to make a url configuration or URLconf. These must be defined within each django app, its good to just name them urls.py within the app"""

from django.urls import path
from . import views


urlpatterns = [
        path("", views.index, name="index"),
            ]

