import requests

class Record:
    domain_name: str
    record_type: str
    name: str
    ip: str

    def __init__(self, domain_name: str, record_type: str, name: str, ip: str):
        self.domain_name = domain_name
        self.record_type = record_type
        self.name = name
        self.ip = ip

    def update_ip(self, ip: str):
        if self.ip != ip:
            self.ip = ip
            return True
        else:
            return False

class DomainRegistratorClient:
    def get_record(self, domain_name: str, record_type: str, name: str) -> Record:
        raise NotImplementedError

    def update_record(self, record: Record):
        raise NotImplementedError

class GoDaddyDomainRegistratorClient(DomainRegistratorClient):
    url = 'https://api.godaddy.com/v1/domains/'

    def __init__(self, key: str, secret_key: str):
        self.key = key
        self.secret_key = secret_key

    def __authorization_header(self):
        return {'Authorization': "sso-key {key}:{secret_key}".format(key = self.key, secret_key = self.secret_key)}

    def get_record(self, domain_name: str, record_type: str, name: str) -> Record:
        url = self.url + "{domain_name}/records/{record_type}/{name}".format(domain_name=domain_name, record_type=record_type, name=name)
        response = requests.get(url, headers = self.__authorization_header())
        
        if response.status_code != 200:
            raise Exception("Bad response from the selected registrator" + response.text)

        return Record(domain_name=domain_name, record_type=record_type, name=name, ip=response.json()[0]["data"])

    def update_record(self, record: Record):
        url = self.url + "{domain_name}/records/{record_type}/{name}".format(domain_name=record.domain_name, record_type=record.record_type, name=record.name)
        response = requests.put(url, headers = self.__authorization_header(), json=[{"data": record.ip}])

        if response.status_code != 200:
            raise Exception("Bad response from the selected registrator" + response.text)