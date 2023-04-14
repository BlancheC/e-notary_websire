import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import db

load_dotenv()

email_api_key = os.environ['EMAIL_API_KEY']

def send_email(to_email, subject, html_content):
    from_email = os.environ['FROM_EMAIL']
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )

    try:
        sg = SendGridAPIClient(email_api_key)
        response = sg.send(message)
        print(f"Email sent to {to_email}, status code: {response.status_code}")

        # Save the email to the database
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO emails (to_email, subject, body)
            VALUES (%s, %s, %s)
        """, (to_email, subject, html_content))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

