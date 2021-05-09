import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "HELLO AMAN !!!!!  Take a break! It has been an 1 min!",
            timeout = 10
        )
        time.sleep(3600)