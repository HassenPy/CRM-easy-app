from django.conf.urls import patterns, url

contact_urls = patterns('',
                        url('^new/$', 'contacts.views.cont_creation',
                            name='contact_new'),
                        url('^$', 'contacts.views.contact_detail',
                            name="contact_detail")
                        )
