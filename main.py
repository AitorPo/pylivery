from clients.catcher import catcher_client
from clients.glovo import glovo_v2_client

catcher_client.set_api_credentials(api_key='api_key', api_secret='api_secret')
glovo_v2_client.set_api_credentials(client_id='client_id', client_secret='client_secret', stage='staging')

if __name__ == '__main__':
    catcher_client.validate_address({})
    glovo_v2_client.validate_address({})
