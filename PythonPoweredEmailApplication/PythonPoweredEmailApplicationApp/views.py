from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def pythonPoweredEmailApplication(request,):
    if request.method == 'POST':
        senderEmailAddress = request.POST['senderEmailAddress']
        receiverEmailAddress = request.POST['receiverEmailAddress']  #receiverEmailAddress
        cc = request.POST['cc']
        attachFiles = request.POST['attachFiles']
        subject = request.POST('subject')
        body = request.POST('body')
        send_mail(
            'settings.EMAIL_HOST',
            senderEmailAddress,
            'settings.EMAIL_HOST_USER',
            receiverEmailAddress,
            'settings.CC',
            [cc],
            'Send Email',  # title
            body,  # body of the message
            'Subject',
            fail_silenty=False,
        )
    return render(request, 'pythonpoweredemailapplication.html')
