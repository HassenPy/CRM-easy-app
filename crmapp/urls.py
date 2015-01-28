from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from marketing.views import HomePage
from subscribers.views import subscriber_view
from accounts.urls import account_urls
from contacts.urls import contact_urls
from contacts.views import cont_creation, ContactDelete
from communications.urls import com_urls
from communications.views import comm_creation

urlpatterns = patterns('',

                       # Admin URL
                       url(r'^admin/',
                           include(admin.site.urls)
                           ),

                       # Marketing pages
                       url(r'^$',
                           HomePage.as_view(),
                           name="home"
                           ),

                       # Subscriber related URLs
                       url(r'^signup/',
                           subscriber_view,
                           name='signup_url'
                           ),

                       # Login/Logout URLs
                       url(r'^login/$',
                           login,
                           {'template_name': 'login.html'}
                           ),
                       url(r'^logout/$',
                           logout,
                           {'next_page': '/login/'}
                           ),

                       # Account related URLs
                       url(r'^account/',
                           include(account_urls)
                           ),

                       # Contact related URLS
                       url(r'^contact/new/$',
                           cont_creation,
                           name='contact_new'
                           ),
                       url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)
                           ),

                       url(r'^contact/(?P<pk>[\w-]+)/delete/$',
                           ContactDelete.as_view(),
                           name='contact_delete'
                           ),

                       # Communication related URLs
                       url(r'^comm/new/$',
                           comm_creation,
                           name='comm_new'
                           ),
                       url(r'^comm/(?P<uuid>[\w-]+)',
                           include(com_urls)
                           ),

                       )
