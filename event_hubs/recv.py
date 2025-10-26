import asyncio

from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore
from azure.identity.aio import DefaultAzureCredential

blob_store='https://mystore553.blob.core.windows.net/'
blob_container='events'
event_hub_fqdn='eventhub553.servicebus.windows.net'
event_hub_name='apphub'

credential=DefaultAzureCredential()

async def on_event(partition_context,event):
    print(f'received event: {event.body_as_str(encoding='utf-8')} from partition with id {partition_context.partition_id}')

    await partition_context.update_checkpoint(event)


async def main():
    checkpoint_store=BlobCheckpointStore(blob_account_url=blob_store,
                                         container_name=blob_container,
                                         credential=credential
                                         
                                         )
    client=EventHubConsumerClient(
        fully_qualified_namespace=event_hub_fqdn,
        eventhub_name=event_hub_name,
        consumer_group='$Default',
        checkpoint_store=checkpoint_store,
        credential=credential
        )
    async with client:
        await client.receive(on_event=on_event,starting_position='-1')
        await credential.close()

if __name__=='__main__':
    asyncio.run(main())