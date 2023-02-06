from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
from .helpers import rishav
import json
class MyAsyncComsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("websocket connected..", event)

        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        print("Message Receive From Client")
        # print(event['text'])
        # await self.send({
        #     'type': 'websocket.send',
        #     'text': 'Message Send To Client'
        # })
        urls = event['text'].split()
        total = len(urls)
        for count, url in enumerate(urls, 1):
            x = rishav(url)
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({
                    'total': total,
                    'count': count,
                    'url': x 
                })
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print("websocket disonnected..", event)
        raise StopConsumer 
    
class MySyncComsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("websocket connected..", event)

        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print("Message Receive From Client", event)
        print(event['text'])
        for i in range(5):
            self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            sleep(1)

    def websocket_disconnect(self, event):
        print("websocket disonnected..", event)
        raise StopConsumer 