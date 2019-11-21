from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import status
from .serializer import notesSerializer
from .models import notes
from rest_framework.response import Response
from django.utils import timezone
import datetime
# Create your views here.
class notesViewSet(ModelViewSet):
    queryset = notes.objects.all()
    serializer_class = notesSerializer
    def create(self,request):
        obj =notes()
        obj.Title=request.data['Title']
        obj.Description=request.data['Description']
        obj.date_created=datetime.datetime.utcnow()
        obj.date_updated=datetime.datetime.now()
        obj.save()
        return Response({"mesage":"Your Note has been Succesfully added to database"},status =status.HTTP_201_CREATED)