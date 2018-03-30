from django.conf.urls import url
from . import views

app_name = 'sms'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<message_id>)', views.detail, name='detail'),
    url(r'^delete$', views.delete_sms, name='delete'),
    url(r'^api/v1/sms$', views.sms_api, name='sms_api'),
]