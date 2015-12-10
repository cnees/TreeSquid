from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^conversation/(?P<root_id>[0-9]+)/$', views.root, name='root'),
	url(r'^conversation/(?P<root_id>[0-9]+)/reply/$', views.replies, name='replies'),
]