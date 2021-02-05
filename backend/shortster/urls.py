from django.urls import path,  include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='shortster API')

urlpatterns = [
    path('api/v1/', include('main.api.urls')),
    path('docs', schema_view)
]
