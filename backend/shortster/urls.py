from django.urls import path,  include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from main.api.views import redirect_view

schema_view = get_swagger_view(title='shortster API')

urlpatterns = [
    path('<str:shortcode>', redirect_view, name="redirect"),
    path('api/v1/', include('main.api.urls')),
    path(' ', schema_view)
]
