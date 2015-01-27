from django.conf.urls import patterns, include, url
from django.contrib import admin

from marketing.views import HomePage
from subscribers.views import subscriber_view
from accounts.urls import account_urls
from contacts.urls import contact_urls
from contacts.views import cont_creation, ContactDelete
from communications.urls import com_urls

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
                       url(r'^account/', include(account_urls)),
                       # Contact related URLS
                       url(r'^contact/new/$', cont_creation,
                           name='contact_new'
                           ),
                       url(r'^contact/(?P<uuid>[\w-]+)/',
                           include(contact_urls)
                           ),

                       url(r'^contact/(?P<pk>[\w-]+)/delete/$',
                           ContactDelete.as_view(),
                           name='contact_delete'
                           ),
                       # Communication related URLs
                       url(r'^comm/(?P<uuid>[\w-]+)',
                           include(com_urls)
                           ),
                       )
