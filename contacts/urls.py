from django.urls import patterns, url

contact_urls = patterns('',
                        url('^$', 'contacts.views.contact_detail',
                            name="contact_detail")
                        )
