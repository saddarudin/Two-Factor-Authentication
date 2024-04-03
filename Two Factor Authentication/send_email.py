from email.message import EmailMessage
import ssl
import smtplib
import password
import otp_generator


def send_mail(mail):
    email_sender = '03480331849s@gmail.com'
    email_password = password.app_password()
    email_receiver = mail

    subject = "One Time Password"
    body = f"Your OTP is {otp_generator.otp()}"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
