from django.urls import path,  include
from django.conf.urls import url
from rest_framework.schemas import get_schema_view

from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from main.api.views import redirect_view

schema_view = get_schema_view(
                                title='CLIPIT API DOCUMENTATION',
                                description='Do you want to leverage our API in your current project? Well, be our guest. Our API is free. No API keys required.',
                                renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
                            )

urlpatterns = [
    path('<str:shortcode>', redirect_view, name="redirect"),
    path('api/v1/', include('main.api.urls')),
    path('', schema_view)
]
