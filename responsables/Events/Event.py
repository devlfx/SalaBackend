subscribers = {}

def subscribe(event_type:str,fn):
    if not event_type in subscribers:
        subscribers[event_type] = set()
    subscribers[event_type].add(fn)

async def post_event(event_type:str, data):
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        await fn(data)
    return 