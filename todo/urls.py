from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from notes import views

router = routers.SimpleRouter()
router.register(r'notes', views.NoteViewSet)


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('notes.urls')),
    url(r'^sms/', include('sms.urls')),
    url(r'^api-auth', include ('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v2/', include((router.urls, 'routers'), namespace='apiv2')),
]
