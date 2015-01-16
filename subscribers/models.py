from django.db import models
from django.contrib.auth.models import User


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
