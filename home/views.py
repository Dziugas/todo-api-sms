from django.shortcuts import render
from notes.models import Notes

from twilio.rest import Client


def index(request):
    latest_note = Notes.objects.latest('date')
    ACCOUNT_SID = "AC4614b91e4db90b0686a0cd932d93b904"
    AUTH_TOKEN = "6a0b6e6378ace0f725335faa92f5409d"

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    messages = client.messages.list()
    latest_sms = messages[0].date_sent
    return render(request, 'home/index.html', {'latest_note':latest_note, 'latest_sms': latest_sms})
