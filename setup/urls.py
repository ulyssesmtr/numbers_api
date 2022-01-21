from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from numbers_api.views import NumberViewSet

router = routers.DefaultRouter()
router.register('numbers', NumberViewSet, basename='Numbers')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
