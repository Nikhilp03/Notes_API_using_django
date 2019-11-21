from rest_framework.routers import DefaultRouter
from django.conf.urls import include,url
from .views import notesViewSet
router=DefaultRouter()
router.register('notes',notesViewSet,base_name='notes')

urlpatterns=[
    url('',include(router.urls))
]