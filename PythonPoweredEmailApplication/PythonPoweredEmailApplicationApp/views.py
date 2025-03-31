from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def pythonPoweredEmailApplication(request,):
    if request.method == 'POST':
        sender_email = request.POST['sender_email']
        recipient_email = request.POST['recipient_email']
        cc_email = request.POST.get('cc_email', '')
        attachment = request.FILES.get('attachment')
        subject = request.POST['subject']
        body = request.POST['body']

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=sender_email,
            to=[recipient_email],
            cc=[cc_email] if cc_email else [],
        )

        if attachment:
            email.attach(attachment.name, attachment.read(), attachment.content_type)

        email.send()
        return HttpResponse("Email sent successfully!")


    return render(request,"pythonpoweredemailapplication.html")
