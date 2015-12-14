from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^about/$', views.about, name='about'),
  url(r'^conversation/(?P<root_id>[0-9]+)/$', views.root, name='root'),
  url(r'^conversation/(?P<root_id>[0-9]+)/reply/$', views.add_reply, name='add_reply'),
  url(r'^conversation/$', views.root, name="root"),
  url(r'^add_root/$', views.add_root, name='add_root'),
  url(r'^register/$', views.register, name='register'),
  url(r'^login/$', views.user_login, name='login'),
  url(r'^logout/$', views.user_logout, name='logout'),
  # Catch all url redirects to index, '/'
  url(r'^.*/$', views.index, name='index'),
]