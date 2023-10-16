import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the GPIO pin for the noise sensor
noise_sensor_pin = 17  # Use the appropriate GPIO pin

# Set the threshold for noise level
threshold = 70
# Email configuration
smtp_server = "eceeemechcse@gmail.com"
smtp_port = 587
smtp_username = "aadhj@gmail.com"
smtp_password = "aadhjAADHJ"
sender_email = "xyz@gmail.com"
recipient_email = "pqrst@gmail.com"

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin as input
GPIO.setup(noise_sensor_pin, GPIO.IN)

def send_email():
    subject = "Noise Pollution Alert"
    body = "Noise level has exceeded the threshold. Take action!"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

try:
    while True:
        # Read the noise level (simulated in this example)
        noise_level = GPIO.input(noise_sensor_pin)

        if noise_level == 1 and noise_level > threshold:
            print("Noise level exceeded the threshold. Sending an email alert.")
            send_email()
        
        time.sleep(1)  # Delay to control data rate

except KeyboardInterrupt:
    print("Script terminated.")
finally:
    GPIO.cleanup()
