from enum import Enum
from decouple import config
from .IOSNotificator import IOSNotificator
from .SimpleCriticalAlertIOS import SimpleCriticalAlertIOS
from .SimpleAlertIOS import SimpleAlertIOS



class IOSNotificationType(Enum):
    SimpleAlert = 1
    SimpleCriticalAlert = 2 

    @property
    def notificator(self):
        if self is IOSNotificationType.SimpleAlert:
            apn_key = config("APPLE_KEY_ID")
            team_id = config("APPLE_TEAM_ID")
            bundle = config("IOS_BUNDLE")
            apn_name = config("APPLE_PUSH_CERT")
            builder = SimpleAlertIOS()
            return IOSNotificator(builder = builder,apns_key_id=apn_key,apns_key_name=apn_name,team_id=team_id,bundle_id=bundle)
        elif self is IOSNotificationType.SimpleCriticalAlert:
            apn_key = config("APPLE_KEY_ID")
            team_id = config("APPLE_TEAM_ID")
            bundle = config("IOS_BUNDLE")
            apn_name = config("APPLE_PUSH_CERT")
            builder = SimpleCriticalAlertIOS()
            return IOSNotificator(builder = builder,apns_key_id=apn_key,apns_key_name=apn_name,team_id=team_id,bundle_id=bundle)