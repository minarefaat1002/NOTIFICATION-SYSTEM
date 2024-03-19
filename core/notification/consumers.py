from channels.generic.websocket import AsyncWebsocketConsumer
from django.template import Context, Template
import json


# websocket consumer
class NotificationConsumer(AsyncWebsocketConsumer):

    # when someone connect
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("notifications", self.channel_name)

    # when soemone disconnects
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notifications", self.channel_name)

    # send notification to all group
    async def send_notification(self, event):
        message = event["message"]

        template = Template('<div class="notification"><p>{{message}}</p></div>')
        context = Context({"message": message})
        rendered_notification = template.render(context)

        await self.send(
            text_data=json.dumps(
                {"type": "notification", "message": rendered_notification}
            )
        )
