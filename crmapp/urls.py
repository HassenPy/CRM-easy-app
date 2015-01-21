from django.conf.urls import patterns, include, url
from django.contrib import admin

from marketing.views import HomePage
from subscribers.views import subscriber_view
from accounts.views import AccountList, account_detail
from accounts.urls import account_urls


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
                           ),
                       # Account related URLs
                       url(r'^account/new/$', 'accounts.views.acc_creation', name='account_new'),
                       url(r'^account/$', AccountList.as_view(), name='account_list'),
                       # Contact related URLS
                       url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),
                       # Communication related URLs
                       )
