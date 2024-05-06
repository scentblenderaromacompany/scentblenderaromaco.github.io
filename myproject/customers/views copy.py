# views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import handle_customer_data

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def shopify_webhook_view(request):
    """
    Handle webhook requests sent from Shopify.
    """
    try:
        verified = verify_webhook(request.body, request.headers.get('X-Shopify-Hmac-Sha256'))
        if verified:
            # Process the webhook data
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid HMAC signature'}, status=403)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
