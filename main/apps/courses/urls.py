from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add', views.add),
    url(r'^(?P<course_id>\d+)/comment', views.comment),
    url(r'^(?P<course_id>\d+)/nComment', views.nComment),
    url(r'^(?P<course_id>\d+)/remove', views.remove),
    url(r'^(?P<course_id>\d+)/delete', views.delete),
]
