import notifications
from notifications.NotificationSender import NotificationSender
from Database.models.models import Informe, Notificacion
class NotificationService:

    def send_notification(self,notification):
        pass


    async def send_critical_notification(self,notification:Notificacion):
        '''
        This method send the notification and recieves a notification object to be send
        It's important to note that these objects were created as a result of register a new inform
        '''
        print(notification.responsable.dispositivos)

        devices = notification.responsable.dispositivos
        inform = notification.informe
        title = inform.titulo
        body = inform.descripcion + " " + inform.formatted_date
        data = { "headers":{"apns_collapse-id":str(inform.id_informe)} }
        data["idInforme"] = notification.id_informe
        for device in devices :
            notifier = NotificationSender(device.tipo_equipo).notifier.SimpleCriticalAlert.notificator
            await notifier.push(device_token= device.token_equipo,title=title,body=body,data=data)



    def send_critical_from_inform():
        pass