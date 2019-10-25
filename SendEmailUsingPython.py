# This code snippet shows how to send email in plain text or in html from Python. 
# How to send image or other file type attachments. How to send to multiple recipients.
# Most importantly from security perspective, how to use environment variables stored in Windows for sensitive information such as password, email address, etc instead of hard-coded in the script itself. This prevents accidental data leakage when sharing codes. 

import os
import smtplib
import imghdr # Python library to determine what image type of file attached
from email.message import EmailMessage

EMAIL_FROM_ADDRESS = os.environ.get('FromMailID')
EMAIL_TO_ADDRESS = os.environ.get('ToMailID')
EMAIL_PASSWORD = os.environ.get('MailPW')

# Uncomment the below statement for sending emails to various recipients
### contacts = ['johndoe@yahoo.com', 'janedoe@yahoo.com']

msg = EmailMessage()
### msg['Subject'] = 'Test Message - Sending from Python' # Sending regular email
msg['Subject'] = 'Check out the ebook'
msg['From'] = EMAIL_FROM_ADDRESS
msg['To'] = EMAIL_TO_ADDRESS # Sending email to one recipient.
# msg['To'] = ', '.join(contacts) # Replace the single email address above for sending email to multiple recipients. Refer to the above 'contacts' variable for a sample list of email addresses.
msg.set_content('This is a plain text email...') # msg.set_content('File attached...')

# The following 8 lines demonstrate user can send html email other than plain text email.
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style='color:SlateGray;'>This is an HTML Email!</h1>
    <body>
</html>
""", subtype='html')

files = ['ebook.pdf']
### files = ['image1.jpg', 'image2.jpg'] # Example of sending multiple image files

for file in files:
    with open(file, 'rb') as f:
        file_Data = f.read()
        # file_type = imghdr.what(f.name) # Check out what image type. Uncomment this statement when sending image file.
        file_name = f.name

    msg.add_attachment(file_Data, maintype='application', subtype='octet-stream', filename=file_name) # Use this to attach files other than image eg, pdf doc
    
    ### msg.add_attachment(file_Data, maintype='application', subtype='octet-stream', filename=file_name) # Use this statement to attach image files

# Instead of using SMTP and port 587 whcih requires additional codes to start tls encryption ie, use SMTP_SSL encryption method at port 465. The 3 lines of code can be removed.
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    ### smtp.ehlo()
    ### smtp.starttls()
    ### smtp.ehlo()
    smtp.login(EMAIL_FROM_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

