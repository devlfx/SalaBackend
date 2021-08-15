from decouple import config
from .AlertBuilder import AlertBuilder
import httpx
import jwt
import time
import os
import asyncio
import json



class IOSNotificator:
    def __init__(self,builder:AlertBuilder, apns_key_id:str = '', apns_key_name:str = '.p8', team_id:str = '', bundle_id:str = ''):
        self.ALGORITHM = 'ES256'
        self.APNS_KEY_ID = apns_key_id
        self.APNS_AUTH_KEY = apns_key_name
        self.TEAM_ID = team_id
        self.BUNDLE_ID = bundle_id
        self.NotificationBuilder = builder

    async def push(self,device_token:str,title:str,body:str,data:dict,sound:str="default"):#, device_token: str, isProduction=True):
        file = open(self.APNS_AUTH_KEY)
        secret = file.read()
        token = jwt.encode({
                    'iss': self.TEAM_ID,
                    'iat': time.time()
                },
                secret,
                algorithm = self.ALGORITHM,
                headers = {
                    'alg': self.ALGORITHM,
                    'kid': self.APNS_KEY_ID,
                }
        )
        path = '/3/device/{0}'.format(device_token)
        request_headers = self.NotificationBuilder.build_headers(token=token,bundle=self.BUNDLE_ID,data=data)
        url = "https://"
        if config("PRODUCTION_MODE",cast=bool,default=False):
            url += 'api.push.apple.com:443'
        else :
            url += 'api.sandbox.push.apple.com:443'    
        url += path
        
        payload_data = self.NotificationBuilder.build_body(title=title,body=body,sound=sound)

        payload = json.dumps(payload_data).encode('utf-8')

        async with httpx.AsyncClient(http2=True) as client:
            response = await client.post(url,headers=request_headers,data=payload)
            


async def _test():
    from .SimpleCriticalAlertIOS import SimpleCriticalAlertIOS
    apn_key = config("APPLE_KEY_ID")

    team_id = config("APPLE_TEAM_ID")

    bundle = config("IOS_BUNDLE")

    apn_name = config("APPLE_PUSH_CERT")

    builder = SimpleCriticalAlertIOS()

    notifier = IOSNotificator(builder = builder,apns_key_id=apn_key,apns_key_name=apn_name,team_id=team_id,bundle_id=bundle)
    
    device_token = "57be78474f6f568b49e530fe4d60273437bb6351a87e7cc2e0944e25d73d9973"
    await notifier.push(device_token=device_token,title="Actualización estado",body="Existe una actualización de estado del paciente",data=None)




if __name__ == "__main__":
    asyncio.run(_test())