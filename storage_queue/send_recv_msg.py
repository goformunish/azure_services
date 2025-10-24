# %%
from azure.storage.blob import BlobServiceClient
from azure.storage.queue import QueueServiceClient

# %%
conn_str_queue='BlobEndpoint=https://mystore553.blob.core.windows.net/;QueueEndpoint=https://mystore553.queue.core.windows.net/;FileEndpoint=https://mystore553.file.core.windows.net/;TableEndpoint=https://mystore553.table.core.windows.net/;SharedAccessSignature=sv=2024-11-04&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2025-10-25T03:54:05Z&st=2025-10-24T19:39:05Z&spr=https&sig=pYTbE2gcASimB%2Fnx5HG6lQ9XdMhXRseLle01i%2FBWtf8%3D'

# %%
blob_service_client=BlobServiceClient.from_connection_string(conn_str_queue)
queue_service_client=QueueServiceClient.from_connection_string(conn_str_queue)

# %%
queue_name='appqueue'
queue_client=queue_service_client.get_queue_client(queue_name)

# %%
for i in range(10):
    message=f'proceed with job_{i}'
    queue_client.send_message(message)
    print(f'message sent: {message}')

# %%
# receive single message
recv=queue_client.receive_message()
print(f'message received: {recv}')

# %%
# message gets read but need to delete explicitly after reading from queue
messages= queue_client.receive_messages(messages_per_page=5)
for msg_btch in  messages.by_page():
    for msg in msg_btch:
        print(f'messages received and content is: {msg.content}')

        # delete the message after processing
        queue_client.delete_message(msg)
        print(f'message deleted from queue: {msg}')

# %%



