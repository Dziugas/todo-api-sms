from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

from todo import twilio_keys


@csrf_exempt
def index(request):
    client = Client(twilio_keys.ACCOUNT_SID, twilio_keys.AUTH_TOKEN)
    messages = client.messages.list()
    number=0
    for message in messages:
        if message.direction=='inbound':
            number +=1
    return render(request, 'sms/index.html', {'messages' : messages, 'number' : number})

def detail(request, message_sid):
    client = Client(twilio_keys.ACCOUNT_SID, twilio_keys.AUTH_TOKEN)
    message = client.messages(message_sid).fetch()
    return render(request, 'sms/detail.html', {'message' : message})

def delete_sms(request):
    client = Client(twilio_keys.ACCOUNT_SID, twilio_keys.AUTH_TOKEN)
    message_id = request.POST.get('message_sid', None)
    client.messages(message_id).delete()
    return redirect('sms:index')



