import requests

class IpClient:
    def get_current_ip(self):
        raise NotImplementedError

class IpifyIpClient(IpClient):
    url = 'https://api.ipify.org?format=json'

    def get_current_ip(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("IP service returned an error" + response.text)
        return response.json()["ip"]
