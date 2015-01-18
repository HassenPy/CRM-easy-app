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
                       url(r'^signup/', subscriber_view, name='signup_url'),
                       # Login/Logout URLs
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'login.html'}
                           ),
                       url(r'^logout/$', 'django.contrib.auth.views.logout',
                           {'next_page': '/login/'}
                           )
                       # Account related URLs
                       # Contact related URLS
                       # Communication related URLs
                       )
