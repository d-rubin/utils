import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_email(sender_email, sender_password, receiver_emails, subject, html_content, smtp_server, smtp_port):
    """
    Sendet eine HTML-E-Mail an mehrere Empfänger.

    Args:
        sender_email (str): Die E-Mail-Adresse des Absenders.
        sender_password (str): Das Passwort des Absenders.
        receiver_emails (list): Eine Liste von E-Mail-Adressen der Empfänger.
        subject (str): Der Betreff der E-Mail.
        html_content (str): Der HTML-Inhalt der E-Mail.
        smtp_server (str): Die Adresse des SMTP-Servers.
        smtp_port (int): Der Port des SMTP-Servers.
    """

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_emails)  # Empfängeradressen als Zeichenkette

    html_part = MIMEText(html_content, "html")
    message.attach(html_part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Verschlüsselung aktivieren
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_emails, message.as_string())  # Liste der Empfänger
        server.quit()
        print("E-Mail wurde erfolgreich an alle Empfänger gesendet!")
    except Exception as e:
        print(f"Fehler beim Senden der E-Mail: {e}")

if __name__ == "__main__":
    smtp_server = ""
    smtp_port = 587  # Oder 465, je nach Konfiguration (587 wird empfohlen)

    sender_email = ""
    sender_password = ""  # Ihr Hetzner-E-Mail-Passwort
    receiver_emails = [""]
    subject = "Test-E-Mail"
    html_content = """
    """

    send_html_email(sender_email, sender_password, receiver_emails, subject, html_content, smtp_server, smtp_port)
