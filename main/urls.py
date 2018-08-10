from django.conf.urls import url
from main.views import *

app_name = 'main'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='list_of_notes'),
    url(r'^api/note$', NoteList.as_view(), name='note_list'),
]
