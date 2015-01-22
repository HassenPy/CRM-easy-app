from django.conf.urls import patterns, url
from .views import AccountList, account_detail, acc_creation


account_urls = patterns('',
                        url(r'^$', AccountList.as_view(),
                            name='account_list'),
                        url(r'^new/$', acc_creation,
                            name='account_new'),
                        url(r'^edit/$', acc_creation,
                            name='account_update'),
                        url(r'^(?P<uuid>[\w-]+)/$', account_detail,
                            name='account_detail'),
                        )
