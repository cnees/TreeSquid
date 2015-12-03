from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /conversations/
	url(r'^$', views.index, name='index'),
	# ex: /conversations/5/
	url(r'^(?P<root_id>[0-9]+)/$', views.root, name='root'),
]