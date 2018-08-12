from rest_framework import generics

from api.models import Note
from api.serializers import NoteSerializer
from api.utils import count_of_unique_words


class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        notes = Note.objects.all()
        return sorted(notes, key=lambda note: count_of_unique_words(note.description))
