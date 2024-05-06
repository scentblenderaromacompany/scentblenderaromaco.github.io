# utils.py
from shopify import Session, ShopifyAPI

def create_shopify_session():
    session = Session( '4b6708-d4.myshopify.com', 'f4c577d4f2ce64b9b02e35c51eefedc3', 'STrappingaintdead69$')
    shopify.ShopifyResource.activate_session(session)
# utils.py
def handle_customer_data(data):
    email = data['customer']['email']
    phone = data['customer']['phone']
    # Process and store this data or send SMS
