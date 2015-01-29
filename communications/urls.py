from django.conf.urls import patterns, url
from .views import comm_details, comm_creation


com_urls = patterns('',
                    url(r'^$', comm_details,
                        name='comm_detail'
                        ),
                    url(r'^/edit$', comm_creation,
                        name='comm_update'
                        ),
                    )
