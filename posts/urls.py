from django.conf.urls import patterns, include, url
from posts.models import Post

urlpatterns = patterns('',
	url(r'^all/$', 'posts.views.posts'),
	url(r'^get/(?P<post_id>\d+)/$', 'posts.views.post'),
	url(r'^create/$', 'posts.views.create'),
)