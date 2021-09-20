from .AlertBuilder import AlertBuilder

class SimpleAlertIOS(AlertBuilder):
    def __init__(self) -> None:
        super().__init__()

    def build_body(self,data:dict = None, title:str = "", body:str = "", sound:str = "default",thread_id:str = None):
        payload_data = {
                    'aps': {
                        'alert': {
                            'title': title,
                            'body': body
                        },
                        'badge': 1,
                    "sound": sound

                    }

                }
        if thread_id:
            payload_data['aps']["thread-id"] = thread_id
        
        if data:
            for key in data:
                if key == "headers": 
                    continue
                payload_data[key] = data.get(key)

        return payload_data

    def build_headers(self,token:str ,bundle:str ,data:dict = None):
        headers = {
            'apns-expiration': '0',
            'apns-priority': '5',
            'apns-topic': bundle,
            'authorization': 'bearer {0}'.format(token.decode('ascii'))
        }

        if (opt_headers := data.get("headers")):
            for key in opt_headers:
                headers[key] = opt_headers[key]
        return headers