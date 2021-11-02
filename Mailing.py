import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'vintasiya@gmail.com'
PASSWORD = 'Ktdfy4er.1706'

def get_contacts(filename):
  names = []
  emails = []
with open(filename, mode='r', encoding='utf-8') as contacts_file:
    for a_contact in contacts_file:
        names.append(a_contact.split()[0])
        emails.append(a_contact.split()[1])
return names, emails

def read_template(filename):
with open(filename, 'r', encoding='utf-8') as template_file:
    template_file_content = template_file.read()
return Template(template_file_content)

def main():
    names, emails = get_contacts('contacts.txt')  # read contacts
    message_template = read_template('message.txt')
  
# set up the SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
  
  # Get each user detail and send the email:
  for name, email in zip(names, emails):
    
    # create a message
    multipart_msg = MIMEMultipart()
   
    # add in the actual person name to the message
    message = message_template.substitute(PERSON_NAME=name.title())
    
    # Prints out the message body for our sake
    print(message)
    
    # setup the parameters of the message
    msg['From'] = MY_ADDRESS
    msg['To'] = email
    msg['Subject'] = "This is TEST"
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier
    s.send_message(msg)
    del msg
    
# Terminate the SMTP session and close the connection
s.quit()
if __name__ == '__main__':
    main()
