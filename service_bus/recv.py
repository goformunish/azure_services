# %%
import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage

# %%
conn_str_nmspc=''
queue_name='appqueue'

# %%
async def run():
    async with ServiceBusClient.from_connection_string(conn_str=conn_str_nmspc,logging_enable=True) as service_client:
        async with service_client:
            receiver=service_client.get_queue_receiver(queue_name=queue_name)
            
            async with receiver:
                received_msgs=await receiver.receive_messages(max_wait_time=5,max_message_count=20)
                for msg in received_msgs:
                    print(f'received: {msg}')
                    await receiver.complete_message(msg) 

# %%
asyncio.run(run())
