from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import handler404, handler500


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fyl_try2.views.home', name='home'),
    # url(r'^fyl_try2/', include('fyl_try2.foo.urls')),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', 'fyl_try2.views.index'),
    url(r'^faq$', 'fyl_try2.views.faq', name='faq'),
    url(r'^about$', 'fyl_try2.views.about', name='about'),
#    url(r'^contact$', 'fyl_try2.views.contact', name='contact'),
    url(r'^us-congress$', 'fyl_try2.views.get_us_congress', name='us-congress'),
    url(r'^political-map$', 'fyl_try2.views.us_congress_pltcl_map', name='us-congress-map'),
    url(r'^us-congress/trends$', 'fyl_try2.views.us_congress_trends', name='us-congress-trends'),
    url(r'^ngrams$', 'fyl_try2.views.us_congress_trends', name='us-congress-trends'),
   
)
handler404 = 'fyl_try2.views.custom_404_view'
#handler500 = 'fyl_try2.views.custom_404_view'