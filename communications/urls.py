from django.conf.urls import patterns, url
from .views import comm_details


com_urls = patterns('',
                    url(r'^$', comm_details,
                        name='comm_detail'
                        ),
                    url(r'^edit/$', comm_details,
                        name='comm_update'
                        ),
                    )
