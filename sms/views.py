from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

from todo import shmeys


@csrf_exempt
def index(request):
    client = Client(shmeys.ACCOUNT_SID, shmeys.AUTH_TOKEN)
    #filtering does not work in this query
    messages = client.messages.list()
    number=0
    for message in messages:
        if message.direction=='inbound':
            number +=1
    return render(request, 'sms/index.html', {'messages' : messages, 'number' : number})

def detail(request, message_sid):
    client = Client(shmeys.ACCOUNT_SID, shmeys.AUTH_TOKEN)
    message = client.messages(message_sid).fetch()
    return render(request, 'sms/detail.html', {'message' : message})

def delete_sms(request, message_sid):
    client = Client(shmeys.ACCOUNT_SID, shmeys.AUTH_TOKEN)
    client.messages(message_sid).delete()
    redirect('sms:index')



