import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content


class SendMail:
    def __init__(self, emailAddress, otp):
        # sg = sendgrid.SendGridAPIClient(api_key=os.environ.get(SENDGRID_API_KEY))
        SENDGRID_API_KEY = "your key"
        sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
        from_email = Email(" your domain address")  # Change to your verified sender
        to_email = To(emailAddress)  # Change to your recipient
        subject = "Sending with SendGrid is Fun"
        content = Content("text/plain", "your otp is "+otp+".")
        mail = Mail(from_email, to_email, subject, content)

        # Get a JSON-ready representation of the Mail object
        mail_json = mail.get()

        # Send an HTTP POST request to /mail/send
        response = sg.client.mail.send.post(request_body=mail_json)
        print(response.status_code)
        print(response.headers)
