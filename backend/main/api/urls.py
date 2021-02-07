from django.urls import path, include
from main.api.views import (
                            shorten_url, 
                            get_url_stats,
                            get_client_urls)


urlpatterns = [
	path("shortcode", shorten_url, name = "shorten-url"),
    path("urls", get_client_urls, name = "list-urls"),
    path('<str:shortcode>/stats', get_url_stats, name="url-stats"),
]
