from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from numbers_api.views import NumberViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Numbers API",
      default_version='v1',
      description="API that provides ordered numbers",
      terms_of_service="#",
      contact=openapi.Contact(email="ulyssesdmnt@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('numbers', NumberViewSet, basename='Numbers')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
