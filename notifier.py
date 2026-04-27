import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENT, EMAIL_SUBJECT_PREFIX

def send_notification(summary):
    """
    Send an email notification with the processed file summary.
    """
    try:
        print(f"📧 Sending email notification...")

        # Build email content
        subject = f"{EMAIL_SUBJECT_PREFIX}: {summary['file']} processed"
        body = f"""
Hello,

A new CSV file has been automatically detected and processed.

─── File Summary ───────────────────────────────
File Name     : {summary['file']}
Processed At  : {summary['processed_at']}
Total Rows    : {summary['total_rows']}
Total Columns : {summary['total_columns']}
Columns       : {', '.join(summary['columns'])}

─── Null Value Report ──────────────────────────
"""
        for col, count in summary['null_counts'].items():
            body += f"{col}: {count} nulls\n"

        body += f"""
─── Basic Statistics ───────────────────────────
{summary['stats']}

─────────────────────────────────────────────────
This is an automated message from Py Task Automator.
        """

        # Build email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECIPIENT
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send via Gmail SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, msg.as_string())

        print(f"✅ Email sent to: {EMAIL_RECIPIENT}")

    except Exception as e:
        print(f"❌ Error sending email: {e}")