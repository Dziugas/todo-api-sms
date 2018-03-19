from rest_framework import serializers
from . import models

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'text',
            'date',
            'author'
        )
        model = models.Notes