from django.conf.urls import patterns, url

account_urls = patterns('',

                        url(r'^$',
                            'accounts.views.account_detail', name='account_detail'
                            ),
                        )
