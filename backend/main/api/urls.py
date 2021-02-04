from django.urls import path, include
from main.api.views import shorten_url, redirect_view


urlpatterns = [
	path("shortcode", shorten_url, name = "shorten-url"),
    path('<str:shortcode>', redirect_view, name="redirect"),
]
