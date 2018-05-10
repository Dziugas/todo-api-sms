from django.conf.urls import url
from . import views

app_name = 'notes'

urlpatterns = [
    #site urls
    url(r'^$', views.index, name='index'),
    url(r'^(?P<note_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<note_id>[0-9]+)/delete$', views.delete_note, name='delete'),
    url(r'^(?P<note_id>[0-9]+)/edit$', views.note_edit, name='note_edit'),

    # API urls
    url(r'^api/v1/notes/$', views.ListCreateNote.as_view(), name='note_list'),
    url(r'^api/v1/notes/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyNote.as_view(),
        name = 'note_detail'
        ),
]