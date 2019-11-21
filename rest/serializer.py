from rest_framework import serializers
from .models import notes
class notesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = notes
        fields =('url','Title','Description','date_created','date_updated')