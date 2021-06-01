import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart





def email_send(reciever):
    message = MIMEMultipart("Headet")
    message["Subject"] = "first email template"
    message["From"] = your email
    message["To"] = reciever
    # this is recoommended for plain text
    # text = """\
    # Hi,
    # How are you?
    # Real Python has many great tutorials:
    # www.realpython.com"""
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <a href="http://www.realpython.com">Real Python</a> 
           has many great tutorials.jkhjkhjhjihkuhuio
        </p>
      </body>
    </html>
    """
    # part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    # message.attach(part1)
    message.attach(part2)

    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login((your email, (your email password)
    server.sendmail(sender email, reciever, message.as_string())

mail_file = open('data/emails.txt', 'r')
emails     = mail_file.read().split('\n')




     
for i in range(2):
     
     for email in emails:
         print(email)
         print('Sending mail to :', email)
         email_send(email) 




