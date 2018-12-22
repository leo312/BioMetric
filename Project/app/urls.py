__author__ = 'leo_0'

from django.conf.urls import url
from app import views

__author__ = 'DELL'

urlpatterns = [
    url(r'^fir', views.fir, name='fir'),
    url(r'^add', views.add, name='add'),
    url(r'^viewlive', views.viewlive, name='viewlive'),
    url(r'^newinfo', views.newinfo, name='newinfo'),
    url(r'^train', views.train, name='train'),




]
