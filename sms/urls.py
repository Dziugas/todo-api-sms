from django.conf.urls import url
from . import views

app_name = 'sms'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^delete$', views.delete_sms, name='delete'),
]