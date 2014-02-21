from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblogging.views.home', name='home'),
    # url(r'^microblogging/', include('microblogging.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^/', 'microblogging.views.login'),
    url(r'^posts/', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'microblogging.views.login'),
    url(r'^accounts/auth/$', 'microblogging.views.auth_view'),
    url(r'^accounts/logout/$', 'microblogging.views.logout'),
    url(r'^accounts/loggedin/$', 'microblogging.views.loggedin'), 
    url(r'^accounts/invalid/$', 'microblogging.views.invalid_login'),
    url(r'^accounts/register/$', 'microblogging.views.register'),
   
)
