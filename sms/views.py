from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

@csrf_exempt
def index(request):

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "AC5c35aba82906314a02e40242af329c0b"
    AUTH_TOKEN = "cd8ce24c9f427e17b92cca8f91bee39c"

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    messages = client.messages.list()
    number = len(messages)
    return render(request, 'sms/index.html', {'messages' : messages, 'number' : number})

def delete_sms(request):
    ACCOUNT_SID = "AC5c35aba82906314a02e40242af329c0b"
    AUTH_TOKEN = "cd8ce24c9f427e17b92cca8f91bee39c"
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message_id = request.POST.get('message_sid', None)
    client.messages(message_id).delete()
    return redirect('sms:index')
