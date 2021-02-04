from django.urls import path, include
from main.api.views import shorten_url


urlpatterns = [
	path("shortcode", shorten_url, name = "shorten-url"),
]
