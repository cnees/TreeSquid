from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /polls/
	url(r'^$', views.index, name='index'),
	# ex: /polls/5/
	url(r'^(?P<root_id>[0-9]+)/$', views.root, name='root'),
	# ex: /polls/5/results/
	url(r'^(?P<root_id>[0-9]+)/replies/$', views.replies, name='replies'),
]