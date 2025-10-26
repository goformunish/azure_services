# %%
conn_str_nmspc=''

# %%
queue_name='dataqueue'

# %%
import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage

# %%
# sending a single message
async def send_single_msg(sender):
    msg=ServiceBusMessage('single message',application_properties={'team': 'ecd'},message_id=1)
    await sender.send_messages(msg)
    print('sent a single message')
    
# sending multiple messages
async def send_a_list_of_messages(sender):
    messages=[ServiceBusMessage(f'message_{i}') for i in range(5)]
    await sender.send_messages(messages)
    print('sent a list of 5 messages')

# %%
async def send_batch_message(sender):
    async with sender:
        batch_msg=await sender.create_message_batch()
        for _ in range(10):
            try:
                batch_msg.add_message(ServiceBusMessage('message inside service bus batch'))
            except ValueError:
                break
        await sender.send_messages(batch_msg)
    print('sent a batch of 10 messages')

async def run():
    async with ServiceBusClient.from_connection_string(conn_str=conn_str_nmspc,logging_enabled=True) as service_client:
        sender=service_client.get_queue_sender(queue_name=queue_name)
        async with sender:
            await send_single_msg(sender)
            await send_a_list_of_messages(sender)
            await send_batch_message(sender)

# %%
asyncio.run(run())
print('done sending a message')
print('===========================')

# %%
