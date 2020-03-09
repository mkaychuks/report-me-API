from django.contrib import admin
from django.urls import path, include, re_path


# for documentation puporses
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Report-Me API",
      default_version='v1',
      description="A SIMPLE CASE REPORTING API",
      contact=openapi.Contact(url='https://github.com/mkaychuks'),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')), # login and logout
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')), # allows for registration
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]