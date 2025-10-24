# %%
from azure.storage.blob import BlobServiceClient
from azure.storage.queue import QueueServiceClient

# %%
conn_str_queue=''

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



