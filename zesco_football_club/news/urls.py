from __future__ import absolute_import

from . import views
from django.conf.urls import url

urlpatterns = [
    # url(r'^$', views.BaseView.as_view(), name='home'),
    url(r'^$', views.BaseView.as_view(), name='list'),
    # url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='list_detail'),

    url(r'^teams/$', views.Homev2.as_view(), name='home2'),


    url(r'^$', views.BaseView.as_view(), name='home'),
    url(r'^news/(?P<slug>[-\w]+)/$', views.NewsDetailView.as_view(), name='datail'),
]
