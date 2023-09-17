from typing import Union

from enums import ClientsEnum
from clients.catcher import catcher_client, CatcherClient
from clients.glovo import glovo_v2_client, GlovoV2Client
from clients.ubereats import uber_eats_client, UberEatsClient

CLIENTS = {
    ClientsEnum.GLOVO.value: glovo_v2_client,
    ClientsEnum.CATCHER.value: catcher_client,
    ClientsEnum.UBER.value: uber_eats_client
}


def get_delivery_client(client: str) -> Union[CatcherClient, GlovoV2Client, UberEatsClient]:
    return CLIENTS[client]
