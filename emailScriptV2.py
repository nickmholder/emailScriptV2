import csv
import requests

def send_email_with_attachment():
    # Mailgun API configuration
    MAILGUN_API_KEY = ''
    YOUR_DOMAIN_NAME = ''

    # File to be attached
    attachment_file = '.pdf'

    # Mailgun API endpoint for sending emails
    mailgun_url = f"https://api.mailgun.net/v3/{YOUR_DOMAIN_NAME}/messages"

    # Read CSV file with recipient information (assuming 'emails.csv' has columns: Name, Email)
    with open('.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract recipient's information
            receiver_name = row['Name']
            receiver_email = row['Email']

            # Mail content with HTML formatting for hyperlink
            sender_name = 'Nick'  # Replace with the sender's name
            sender_email = ''  # Replace with your sender email
            reply_to_email = ''  # Replace with your actual email for replies
            subject = ""
            html_content = f"""
                <html>
                <body>
                    <p>Good Afternoon{receiver_name},</p>
                </body>
                </html>
            """

            # Mailgun request payload with sender's name
            payload = {
                'from': f'{sender_name} <{sender_email}>',
                'to': receiver_email,
                'subject': subject,
                'html': html_content,
                'h:Reply-To': reply_to_email  # Adding the 'Reply-To' header
            }

            # Attach the file (if available)
            try:
                with open(attachment_file, 'rb') as attachment:
                    files = [("attachment", (attachment_file, attachment))]
                    response = requests.post(
                        mailgun_url,
                        auth=('api', MAILGUN_API_KEY),
                        files=files,
                        data=payload
                    )

                    if response.status_code == 200:
                        print(f"Email sent successfully to {receiver_name}!")
                    else:
                        print(f"Failed to send email to {receiver_name}. Status code: {response.status_code}")
            except Exception as e:
                print(f"Error sending email to {receiver_name}: {e}")

# Call the function to send emails with attachments and hyperlinks
send_email_with_attachment()