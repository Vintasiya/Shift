import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FROM_EMAIL = 'vin***iya@gmail.com'
MY_PASSWORD = '************'

def get_users(file_name):
  names = []
  emails = []
  with open(file_name, mode='r', encoding='utf-8') as user_file:
    for user_info in user_file:
      names.append(user_info.split()[0])
      emails.append(user_info.split()[1])
  return names, emails

def parse_template(file_name):
  with open(file_name, 'r', encoding='utf-8') as msg_template:
    msg_template_content = msg_template.read()
  return Template(msg_template_content)

def main():
  # read user details
  names, emails = get_users('contacts.txt')
  message_template = parse_template('message.txt')
  
  # set up the SMTP server
  smtp_server = smtplib.SMTP(host='smtp.gmail.com', port=587)
  smtp_server.starttls()
  smtp_server.login(FROM_EMAIL, MY_PASSWORD)
  
  # Get each user detail and send the email:
  for name, email in zip(names, emails):
    
    # create a message
    multipart_msg = MIMEMultipart()
   
    # add in the actual person name to the message
    template message = message_template.substitute(USER_NAME=name.title())
    
    # Prints out the message body for our sake
    print(message)
    
    # setup the parameters of the message
    multipart_msg['From']=FROM_EMAIL
    multipart_msg['To']=email
    multipart_msg['Subject']="JournalDev Subject"
    
    # add in the message body
    multipart_msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier
    smtp_server.send_message(multipart_msg) del multipart_msg
    
# Terminate the SMTP session and close the connection
smtp_server.quit() if __name__ == '__main__':
  main()
