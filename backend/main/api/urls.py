from django.urls import path, include
from main.api.views import (
                            shorten_url, 
                            redirect_view,
                            get_url_stats)


urlpatterns = [
	path("shortcode", shorten_url, name = "shorten-url"),
    path('<str:shortcode>', redirect_view, name="redirect"),
    path('<str:shortcode>/stats', get_url_stats, name="url-stats"),
]
