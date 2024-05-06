from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
import hmac
import hashlib
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging

# Setup logging
logger = logging.getLogger(__name__)

class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for managing Customers.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

def verify_webhook(data, hmac_header):
    """
    Verify the Shopify webhook HMAC to authenticate requests.
    
    Args:
    data (bytes): The request body in bytes received from Shopify.
    hmac_header (str): The HMAC header received from Shopify.

    Returns:
    bool: True if the verification passes, False otherwise.
    """
    try:
        secret = bytes(settings.SHOPIFY_API_SECRET, 'utf-8')
        hash = hmac.new(secret, data, hashlib.sha256)
        return hmac.compare_digest(hash.hexdigest(), hmac_header)
    except Exception as e:
        logger.error("Failed to verify webhook signature: %s", e)
        return False

@csrf_exempt
def shopify_webhook(request):
    """
    Handle incoming Shopify webhooks.

    This view exempts CSRF since Shopify doesn't send a CSRF token.
    """
    hmac_header = request.headers.get('X-Shopify-Hmac-Sha256')
    if hmac_header is None:
        return HttpResponse("Unauthorized: No HMAC header found", status=401)

    verified = verify_webhook(request.body, hmac_header)
    if verified:
        # Process the valid webhook here
        # Example: Update database, send notifications, etc.
        return HttpResponse("Webhook processed successfully", status=200)
    else:
        return HttpResponse("Unauthorized: HMAC verification failed", status=401)
