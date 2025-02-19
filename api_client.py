import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, path, data):
        response = requests.post(self.base_url + path, json=data)
        response.raise_for_status()
        return response.json()
    


class LangBackend:
    def __init__(self, api_client):
        self.api_client = api_client

    def save_vocab(self, vocab):
        return self.api_client.post('/vocab', vocab)
    