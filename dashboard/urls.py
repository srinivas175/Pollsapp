from django.conf.urls import url

from .views import *

app_name = 'dashboard'
urlpatterns = [
    url(r'^$', home, name='dashboard'),
]