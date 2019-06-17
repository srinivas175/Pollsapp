from django.conf.urls import url

from .views import *

app_name = 'polls'

urlpatterns = [
    url(r'^$', questions, name='questions'),
    url(r'^(?P<question_id>\d+)/$', detail, name='detail'),
    url(r'^(?P<question_id>\d+)/vote/$', vote, name='vote'),
    url(r'^(?P<question_id>\d+)/results/$', results, name='results'),
]