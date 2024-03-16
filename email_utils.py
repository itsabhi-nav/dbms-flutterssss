import smtplib
import os
from email.message import EmailMessage

def sendEmail(to, sub, msg, GMAIL_ID, GMAIL_PSWD, attachment=None):
    try:
        print(f"Email to {to} sent with subject: {sub} and message: {msg}")
        em = EmailMessage()
        em['From'] = GMAIL_ID
        em['To'] = to
        em['Subject'] = sub
        em.set_content(msg)

        if attachment:
            with open(attachment, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(attachment)
            em.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP('smtp.gmail.com', 587) as context:
            context.starttls()
            context.login(GMAIL_ID, GMAIL_PSWD)
            context.send_message(em)
        print(f"Email sent to {to}")
        return True  # Return True if email sent successfully
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False  # Return False if email sending fails

if __name__ == "__main__":
    # Example usage for testing
    GMAIL_ID = os.getenv('GMAIL_ID')
    GMAIL_PSWD = os.getenv('GMAIL_PSWD')
    to_email = "recipient@example.com"
    subject = "Test email with attachment"
    message = "This is a test email with an attachment."
    attachment_path = "path/to/your/attachment/file.jpg"
    status = sendEmail(to_email, subject, message, GMAIL_ID, GMAIL_PSWD, attachment_path)
    if status:
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
