import unittest
from unittest.mock import MagicMock

from app.App import UpdaterProperties, DnsUpdater
from app.client.domain_registrator import Record, DomainRegistratorClient
from app.client.ip_client import IpClient


class AppTest(unittest.TestCase):
    update_properties = UpdaterProperties(
        domain_name='letscode.dk',
        record_type='A',
        record_name='record-1'
    )

    def test_should_update_dns_record_if_ip_is_different(self):
        ip_client = IpClient()
        registrator_client = DomainRegistratorClient()

        ip = '127.0.0.1'
        record = Record(
            domain_name='letscode.dk',
            record_type='A',
            name='record-1',
            ip=ip
        )

        ip_client.get_current_ip = MagicMock(return_value='127.0.0.3')
        registrator_client.get_record = MagicMock(return_value=record)
        registrator_client.update_record = MagicMock()

        app = DnsUpdater(ip_client=ip_client, domain_registrator_client=registrator_client,
                         properties=self.update_properties)

        app.update()

        registrator_client.update_record.assert_called_once()

    def test_should_not_update_dns_record_if_ip_is_not_different(self):
        ip_client = IpClient()
        registrator_client = DomainRegistratorClient()

        ip = '127.0.0.1'
        record = Record(
            domain_name='letscode.dk',
            record_type='A',
            name='record-1',
            ip=ip
        )

        ip_client.get_current_ip = MagicMock(return_value=ip)
        registrator_client.get_record = MagicMock(return_value=record)
        registrator_client.update_record = MagicMock()

        app = DnsUpdater(ip_client=ip_client, domain_registrator_client=registrator_client,
                         properties=self.update_properties)

        app.update()

        registrator_client.update_record.assert_not_called()
