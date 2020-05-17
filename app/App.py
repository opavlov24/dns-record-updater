import logging

from app.client.domain_registrator import DomainRegistratorClient, Record
from app.client.ip_client import IpClient


class UpdaterProperties:
    domain_name: str
    record_type: str
    record_name: str

    def __init__(self, domain_name: str, record_type: str, record_name: str):
        self.domain_name = domain_name
        self.record_type = record_type
        self.record_name = record_name


class DnsUpdater:
    def __init__(self, ip_client: IpClient, domain_registrator_client: DomainRegistratorClient,
                 properties: UpdaterProperties):
        self.ip_client = ip_client
        self.domain_registrator_client = domain_registrator_client
        self.properties = properties

    def update(self):
        current_ip: str = self.ip_client.get_current_ip()
        record: Record = self.domain_registrator_client.get_record(self.properties.domain_name,
                                                                   self.properties.record_type,
                                                                   self.properties.record_name)
        if record.update_ip(current_ip):
            self.domain_registrator_client.update_record(record)
            logging.info("The dns record has been updated. The new IP address is set to %s", current_ip)
        else:
            logging.debug("The dns record has not been updated because the IP wasn't changed.")
