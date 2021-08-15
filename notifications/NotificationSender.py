from enum import Enum
from notifications.IOS import IOSNotificationType


class NotificationSender(Enum):
    IOS = 1
    ANDROID = 2
    WEB = 3
    EMAIL = 4

    @property
    def notifier(self):
        if self is NotificationSender.IOS:
            return IOSNotificationType
        elif self is NotificationSender.ANDROID:
            print("Android")
        elif self is NotificationSender.WEB:
            print("WEB")
        elif self is NotificationSender.EMAIL:
            print("EMAIL")


if __name__ == "__main__":
    NotificationSender.IOS.notifier
    NotificationSender.ANDROID.notifier
    NotificationSender.WEB.notifier
    NotificationSender.EMAIL.notifier