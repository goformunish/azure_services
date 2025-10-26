import asyncio
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from azure.identity.aio import DefaultAzureCredential
from datetime import datetime

event_hub_fqdn='eventhub553.servicebus.windows.net'
event_hub_name='datahub'

credential=DefaultAzureCredential()

async def run():
    producer=EventHubProducerClient(fully_qualified_namespace=event_hub_fqdn,
                                    eventhub_name=event_hub_name,
                                    credential=credential
                                    
                                    )
    print('producer client created successfully')

    async with producer:
        event_dt_btch= await producer.create_batch()
        event_dt_btch.add(EventData(f'{datetime.now()}: first event'))
        event_dt_btch.add(EventData(f'{datetime.now()}: second event'))
        event_dt_btch.add(EventData(f'{datetime.now()}: third event'))

        await producer.send_batch(event_dt_btch)
        print(f'events produced successfully')

        await credential.close()

asyncio.run(run())
