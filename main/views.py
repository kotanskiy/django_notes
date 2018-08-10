from django.views.generic import TemplateView
from rest_framework import generics
from main.forms import NoteForm
from main.models import Note
from main.serializers import NoteSerializer
from main.utils import count_of_unique_words


class IndexView(TemplateView):
    template_name = 'main/notes_list.html'

    def get_context_data(self, **kwargs):
        form = NoteForm()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context


class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        notes = Note.objects.all()
        return sorted(notes, key=lambda note: count_of_unique_words(note.description))



