import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import certifi

import credentials

def create_image_attachment(path: str) -> MIMEImage:
    with open(path, "rb") as image:
        mime_image = MIMEImage(image.read())
        mime_image.add_header("Content-Disposition", f'attachment; filename={path}')
        return mime_image

def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    host: str = 'smtp.gmail.com'
    port: int = 587

    context = ssl.create_default_context(cafile=certifi.where())

    with smtplib.SMTP(host, port) as server:
        print('Logging in...')
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(credentials.EMAIL, credentials.PASSWORD)

        # Preparing message
        print('Attempting to send email...')
        msg = MIMEMultipart()
        msg['From'] = credentials.EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if image:
            file: MIMEImage = create_image_attachment(image)
            msg.attach(file)

        server.sendmail(from_addr=credentials.EMAIL, to_addrs=to_email, msg=msg.as_string())

        # Success message
        print('SENT~!')


if __name__ == '__main__':
    send_email(to_email='samplereceiver@gmail.com',
               subject='Bro wassup',
               body='Hello, bro',
               image='troll.png')


