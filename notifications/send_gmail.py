import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_gmail(mail_content, sender_addr, recv_addrs, subject_content):
    '''
    #param mail_content: Sending content 
    #param recv_addrs: Recipients 
    #param sender_addr: Sender
    #param send_passwd: App password(16-bit)
    '''
    
    message = MIMEMultipart()
    message['From'] = sender_addr
    message['To'] = recv_addrs
    message['Subject'] = subject_content
    message.attach(MIMEText(mail_content, 'plain'))
    #Connect smtp server
    session = smtplib.SMTP_SSL('smtp.gmail.com:465')
    #Login gmail
    send_passwd = os.environ["APP_PASSWD"]
    session.login(sender_addr, send_passwd)
    #Transfer message content to text
    text = message.as_string()
    #Send email
    session.sendmail(message['From'], message['To'].split(","), text)
    print("send {} successfully".format(message['To']))
    #close connection
    session.quit()

mail_content = '''
Just a test email!
'''
subject_content = "It's a test, please ignore it, thanks!"
#Test multi recipients
to_addrs = "chezhang@redhat.com,rioliu@redhat.com,wewang@redhat.com"

if __name__ == '__main__':
    send_gmail(mail_content, "wewang@redhat.com", to_addrs, subject_content)
