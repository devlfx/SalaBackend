import notifications
from notifications.NotificationSender import NotificationSender
from Database.models.models import Informe, Notificacion
class NotificationService:

    def send_notification(self,notification):
        pass


    async def send_critical_notification(self,notification:Notificacion):
        print(notification.responsable.dispositivos)

        devices = notification.responsable.dispositivos
        inform = notification.informe
        title = inform.titulo
        body = inform.descripcion + " " + inform.formatted_date
        data = { "headers":{"apns_collapse-id":str(inform.id_informe)} }
        for device in devices :
            notifier = NotificationSender(device.tipo_equipo).notifier.SimpleCriticalAlert.notificator
            await notifier.push(device_token= device.token_equipo,title=title,body=body,data=data)



    def send_critical_from_inform():
        pass