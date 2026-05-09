from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'urls', views.URLShortenerViewSet, basename='url')

urlpatterns = router.urls