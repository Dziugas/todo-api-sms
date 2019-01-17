from django.shortcuts import render, redirect

from twilio.rest import Client

from django.views.decorators.csrf import csrf_exempt

ACCOUNT_SID = "AC4614b91e4db90b0686a0cd932d93b904"
AUTH_TOKEN = "6a0b6e6378ace0f725335faa92f5409d"

@csrf_exempt
def index(request):

    # To find these visit https://www.twilio.com/user/account


    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    messages = client.messages.list()
    number = len(messages)
    return render(request, 'sms/index.html', {'messages' : messages, 'number' : number})

def detail(request, message_sid):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages(message_sid).fetch()
    return render(request, 'sms/detail.html', {'message' : message})

def delete_sms(request):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message_id = request.POST.get('message_sid', None)
    client.messages(message_id).delete()
    return redirect('sms:index')



