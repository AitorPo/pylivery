from clients.catcher import catcher_client

if __name__ == '__main__':
    catcher_client.set_api_credentials(api_key='api_key', api_secret='api_secret')
    catcher_client.authorize()

