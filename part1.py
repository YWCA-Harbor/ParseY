import datetime
import settings
import imaplib
import email
import os

user = input('Please type your email from where to extract:')
password = input('Please type the password associated with the email:')
imap_url = 'imap.gmail.com'


def auth(user, password, imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)
    return con
# extracts the body from the email


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
# allows you to download attachments


def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data
# extracts emails from byte array


def loop_emails(msgs):
    today = datetime.date.today()
    file_name = settings.file_name + '-%s' % today
    file_output = open(file_name + '.txt', "w")

    for msg in msgs:
        email_body = get_body(email.message_from_bytes(msg[0][1]))
        file_output.write(email_body.decode('utf-8'))

    file_output.close()
# prints messages from email body


def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = user_email.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs


user_email = auth(user, password, imap_url)
user_email.select('INBOX')

if user_email:
    sender = input('Enter the senders email:')
    msgs = get_emails(search('FROM', sender, user_email))
    settings.part1_globals()
    loop_emails(msgs)
else:
    print('Allow third party apps to access the email account in account settings')
