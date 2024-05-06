from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, shopify_webhook
from django.views.decorators.csrf import csrf_exempt

# Setup a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')

# Define the urlpatterns for the router and additional paths
urlpatterns = [
    path('', include(router.urls)),  # Includes router generated URL patterns
    path('shopify_webhook/', csrf_exempt(shopify_webhook), name='shopify_webhook'),
]
