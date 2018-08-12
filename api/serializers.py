from rest_framework import serializers

from api.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'name', 'description', 'created')

    created = serializers.DateTimeField(format='%d.%m %H:%M', read_only=True)
