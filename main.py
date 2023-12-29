import os
import time
import sys
import plyer

def send_notification(title, message):
  """Sends a notification to the macOS Notification Center.

  Args:
    title: The title of the notification.
    message: The message of the notification.
  """

  command = f"osascript -e 'display notification \"{title}\" with title \"{message}\"'".encode()
  os.system(command)

if sys.platform == "darwin":
    while True:
        time.sleep(60*25)
        send_notification("DRINK WATER NOW!")
else:
    while True:
        plyer.notification.notify(
            title = "Drink Water",
            message = "DRINK WATER NOW!",
            timeout = 10
        )          


