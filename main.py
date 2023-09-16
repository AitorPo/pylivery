from clients.catcher import catcher_client
from clients.glovo import glovo_v2_client
from clients.ubereats import uber_eats_client

catcher_client.set_api_credentials(api_key='api_key', api_secret='api_secret')
glovo_v2_client.set_api_credentials(
    client_id='client_id', client_secret='client_secret', stage='staging'
)
uber_eats_client.set_api_credentials(
    client_id='client_id', client_secret='client_secret', customer_id='customer_id'
)

if __name__ == '__main__':
    uber_eats_client.validate_address({})
    glovo_v2_client.validate_address({})
    catcher_client.validate_address({})
