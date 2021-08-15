from collections import namedtuple

APNS_RESPONSE_CODES = {
    'Success': 200,
    'BadRequest': 400,
    'TokenError': 403, 
    'MethodNotAllowed': 405,
    'TokenInactive': 410,
    'PayloadTooLarge': 413,
    'TooManyRequests': 429,
    'InternalServerError': 500, 
    'ServerUnavailable': 503,
}


APNSResponseStruct = namedtuple('APNSResponseStruct', APNS_RESPONSE_CODES.keys())
APNSResponse = APNSResponseStruct(**APNS_RESPONSE_CODES)