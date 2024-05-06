from django.db import models

class Customer(models.Model):
    """
    Model to represent a customer with their contact preferences.
    """
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    opt_in_emails = models.BooleanField(default=False)
    opt_in_sms = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}"
