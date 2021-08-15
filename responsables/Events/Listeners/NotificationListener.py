import notifications
from responsables.Services import NotificationService
from responsables.Events.Event import subscribe
from Database.models.models import Informe


async def handle_inform_created_event(inform:Informe):
    service = NotificationService()
    for notification in inform.notificaciones:
        await service.send_critical_notification(notification)
    print("evento")


def set_up_notification_events():
    subscribe("inform_created",handle_inform_created_event) 