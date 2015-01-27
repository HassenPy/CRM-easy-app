from django.conf.urls import patterns, url
from .views import com_details
com_urls = patterns('',
                    url(r'^$', com_details,
                        name='com_detail'
                        ),
                    )
