from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

@csrf_exempt
def index(request):
    #twiml = '<Response><Message>responsas</Message></Response>'
    #return HttpResponse(twiml, content_type='text/xml')

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "AC5c35aba82906314a02e40242af329c0b"
    AUTH_TOKEN = "cd8ce24c9f427e17b92cca8f91bee39c"

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    resources = client.messages.list()
    return render(request, 'sms/index.html', {'resources' : resources})
