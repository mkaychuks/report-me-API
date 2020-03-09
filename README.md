# report-me-API
A basic Django REST framework that allows people report cases online, it a very basic/semi-intermediate DRF-API

I made use of the following packages, most of which are third-party

```
django version == 2.2.2
django-allauth 
django-rest-auth
djangorestframework
drf-yasg
```


In my exploring to find a documentation tool, I learnt about `drf-yasg` which is a nice third-party package, thanks to the maintainers and the contributors

### Basic usage of `drf-yasg` package
As a learnt from the official documentation, `drf-yasg` is quite easy to intergrate (if you want the basic functionalities though..

#### Installations
In a virtual environment type the following `pip install drf-yasg`. Then add the `drf_yasg` in your INSTALLED_APPS in the project_level `settings.py`

In the project_level `urls.py` add the following
```python
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Report-Me API",
      default_version='v1',
      description="A SIMPLE CASE REPORTING API",
      contact=openapi.Contact(url='*fill your info here'),
      license=openapi.License(name="**fill your licence type"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

where the options of **title, default_version, description** is editable to your choice..

### codeNEWBIE.. :grin:
### pythonDEV.. :computer:
