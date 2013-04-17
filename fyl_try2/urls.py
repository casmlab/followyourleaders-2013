from django.conf.urls import patterns, include, url
from django.conf import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fyl_try2.views.home', name='home'),
    # url(r'^fyl_try2/', include('fyl_try2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', 'fyl_try2.views.index'),
    url(r'^faq$', 'fyl_try2.views.faq', name='faq'),
    url(r'^about$', 'fyl_try2.views.about', name='about'),
#    url(r'^contact$', 'fyl_try2.views.contact', name='contact'),
    url(r'^us-congress$', 'fyl_try2.views.get_us_congress', name='us-congress'),
    url(r'^us-congress-political-map$', 'fyl_try2.views.us_congress_pltcl_map', name='us-congress-map'),
    url(r'^us-congress-trends$', 'fyl_try2.views.us_congress_trends', name='us-congress-trends'),

    
)
