from django.conf.urls import url

from api.views import NoteList

app_name = 'api'

urlpatterns = [
    url(r'^note$', NoteList.as_view(), name='note'),
]
