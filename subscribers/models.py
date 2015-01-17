from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

import stripe


class Subscriber(models.Model):

    user_rec = models.ForeignKey(User)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'subscribers'

    def __unicode(self):
        return u"%s's subscription info" % self.user_rec

    def charge(self, request, email, fee):
        # Set your secret key: remember to change this to your live secret key
        # in production. See your keys here https://manage.stripe.com/account
        stripe_api_key = settings.STRIPE_SECRET_KEY

        token = request.POST['stripeToken']

        #create a customer
        stripe_customer = stripe.Customer.create(
            card=token,
            description=email)

        #save the stripe id to the customer's profile
        self.stripe_id = stripe.customer_id
        self.save()

        #charge the customer instead of the car
        stripe.Charge.create(
            amount=fee,
            currency="usd",
            customer=stripe_customer.id)

        return stripe_customer
