from django.conf.urls import url
from . import views

app_name = 'notes'

urlpatterns = [
    #site urls
    url(r'^notes/$', views.index, name='index'),
    url(r'^notes/(?P<note_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^notes/(?P<note_id>[0-9]+)/delete$', views.delete_note, name='delete'),
    url(r'^notes/(?P<note_id>[0-9]+)/edit$', views.note_edit, name='note_edit'),

    # API urls
    url(r'^api/$', views.ListCreateNote.as_view(), name='api'),

]