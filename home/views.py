from django.shortcuts import render
from notes.models import Notes

from twilio.rest import Client
from todo import shmeys


def index(request):
    latest_note = Notes.objects.latest('date')

    client = Client(shmeys.ACCOUNT_SID, shmeys.AUTH_TOKEN)
    messages = client.messages.list()
    latest_sms = messages[0].date_sent
    return render(request, 'home/index.html', {'latest_note':latest_note, 'latest_sms': latest_sms})