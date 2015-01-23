from django.conf.urls import patterns, url
from .views import cont_creation, contact_detail


contact_urls = patterns('',
                        url(r'^$', contact_detail,
                            name='contact_detail'),
                        )
