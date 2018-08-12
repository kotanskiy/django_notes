from django.conf.urls import url
from webface.views import *


app_name = 'webface'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]
