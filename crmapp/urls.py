from django.conf.urls import patterns, include, url
from django.contrib import admin
from marketing.views import HomePage
from subscribers.views import subscriber_view


urlpatterns = patterns('',

                       # Admin URL
                       url(r'^admin/', include(admin.site.urls)),
                       # Marketing pages
                       url(r'^$', HomePage.as_view(), name="home"),
                       # Subscriber related URLs
                       url(r'^signup/', subscriber_view, name='signup_url')
                       # Login/Logout URLs
                       # Account related URLs
                       # Contact related URLS
                       # Communication related URLs
                       )
