from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import EmailMessage
from django.conf import settings
import re

# Create your views here.
def is_valid_email(email):
    """ Check if the email is properly formatted """
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_regex, email)
def pythonPoweredEmailApplication(request,):
    if request.method == 'POST':
        sender_email_address = request.POST['sender_email_address']
        recipient_email_address = request.POST['recipient_email_address']
        cc = request.POST.get('cc', '')
        # attachment = request.FILES.get('attachments')
        subject = request.POST['subject']
        body = request.POST['body']

        # Convert comma-separated emails into a list
        cc_email_list = [email.strip() for email in cc.split(",") if email.strip()]

        # Validate all CC emails and remove invalid ones
        valid_cc_emails = [email for email in cc_email_list if is_valid_email(email)]

        # Ensure recipient email is also valid
        if not is_valid_email(recipient_email_address):
            return HttpResponse("Invalid recipient email format!", status=400)
        if not is_valid_email(sender_email_address):
            return HttpResponse("Invalid sender email format!", status=400)

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=sender_email_address,
            to=[recipient_email_address],
            cc=valid_cc_emails,
        )

        # Handle multiple attachments
        for attachment in request.FILES.getlist("attachments"):
            email.attach(attachment.name, attachment.read(), attachment.content_type)

        email.send()
        return HttpResponse("Email sent successfully!")


    return render(request,"pythonpoweredemailapplication.html")
