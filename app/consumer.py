# from channels.generic.websocket import AsyncJsonWebsocketConsumer
# import json
# from models import Person
# from channels.db import database_sync_to_async
# class ShowUpdate(AsyncJsonWebsocketConsumer):
    
  
    
#     async def connect(self):
#         # self.groupname="Updates"
#         # await self.channel_layer.group_add(
#         #     self.groupname,
#         #     self.channel_name
#         # )


#       self.heading = await database_sync_to_async(self.GetData)()



#     async def disconnect(self,close_code):
#         pass


#     async def receive(self, text_data):
#         print(">>>>>>>>",text_data)
#         pass
        
#     def GetData(self):
#         return Person.objects.all()


