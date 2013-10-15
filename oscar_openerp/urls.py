from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from oscar.app import application

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oscar_openerp.views.home', name='home'),
    # url(r'^oscar_openerp/', include('oscar_openerp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'', include(application.urls)),
)#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#import ipdb; ipdb.set_trace()
'''
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True,
        }),
    )
'''
'''
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# The rest of my urls here...
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
'''

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
                            
   )
