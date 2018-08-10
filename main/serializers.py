from rest_framework import serializers

from main.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'name', 'description', 'create_date')

    create_date = serializers.DateTimeField(format='%d.%m.%y %H:%M')
