from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def pythonPoweredEmailApplication(request,):
    if request.method == 'POST':
        # senderEmailAddress = request.POST['senderEmailAddress']
        receiverEmailAddress = request.POST['email']  #receiverEmailAddress
        # cc = request.POST['cc']
        # attachFiles = request.POST['attachFiles']
        subject = request.POST('subject')
        body = request.POST('body')
        send = request.POST('send')
        send_mail(
            'Send Email', #title
            body, #body of the message
            'settings.EMAIL_HOST_USER',
            ['bolosbolosmpjcss@gmail.com', 'n01297959@humbermail.ca'],
            fail_silenty=False,
        )
    return render(request, 'pythonpoweredemailapplication.html')
