# customers/utils.py
from twilio.rest import Client
from django.conf import settings
import logging

# Configure logger for the module
logger = logging.getLogger(__name__)

def send_sms(to, message):
    """
    Sends an SMS message to a specified phone number using Twilio's SMS API.

    Args:
    to (str): The phone number to send the SMS to.
    message (str): The message to be sent.

    Returns:
    bool: True if the SMS was sent successfully, False otherwise.
    """
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to
        )
        logger.info(f"SMS successfully sent to {to}")
        return True
    except Exception as e:
        logger.error(f"Failed to send SMS to {to}: {e}")
        return False
