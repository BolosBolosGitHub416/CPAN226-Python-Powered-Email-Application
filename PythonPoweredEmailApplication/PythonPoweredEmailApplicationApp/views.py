from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import EmailMessage
from django.conf import settings
import re

# Create your views here.
# View to check any valid sender or recipient email
def is_valid_email(email):
    # Check if the recipient or sender email is properly formatted through email regex
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_regex, email)
# Main View of PythonPoweredEmailApplication to handle SMTP email transfer between the
# sender email and the recipient and CC recipient emails
def pythonPoweredEmailApplication(request,):
    if request.method == 'POST':
        sender_email_address = request.POST['sender_email_address']
        recipient_email_address = request.POST['recipient_email_address']
        cc = request.POST.get('cc', '')
        # attachment = request.FILES.get('attachments')
        subject = request.POST['subject']
        body = request.POST['body']

        # Convert comma-separated emails into a email list
        cc_email_list = [email.strip() for email in cc.split(",") if email.strip()]

        # Validate all CC emails and remove invalid ones
        valid_cc_emails = [email for email in cc_email_list if is_valid_email(email)]

        # Ensure sender email address is valid
        if not is_valid_email(sender_email_address):
            return HttpResponse("Invalid sender email address format!", status=400)

        # Ensure recipient email address is valid
        if not is_valid_email(recipient_email_address):
            return HttpResponse("Invalid recipient email address format!", status=400)

        # email - EmailMessage - Python - Django - object
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
        # The sender email sends the email to the recipient email through SMTP - Google
        email.send()
        # Returns an HTTP response confirming the successful email transfer to the recipient email
        return HttpResponse("Email sent successfully!")

    # Returns a render of the pythonpoweredemailapplication.html template file with the request
    return render(request,"pythonpoweredemailapplication.html")
