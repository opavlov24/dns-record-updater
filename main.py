import logging
import os
import schedule
import time

from app.App import DnsUpdater, UpdaterProperties
from app.client.domain_registrator import GoDaddyDomainRegistratorClient
from app.client.ip_client import IpifyIpClient

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    properties = UpdaterProperties(
        domain_name=os.environ["DUPDATER_DOMAIN_NAME"],
        record_type=os.environ["DUPDATER_RECORD_TYPE"],
        record_name=os.environ["DUPDATER_RECORD_NAME"]
    )
    registrator_client = GoDaddyDomainRegistratorClient(
        key=os.environ["DUPDATER_GO_DADDY_KEY"],
        secret_key=os.environ["DUPDATER_GO_DADDY_SECRET_KEY"]
    )
    ip_client = IpifyIpClient()
    app = DnsUpdater(
        ip_client=ip_client,
        domain_registrator_client=registrator_client,
        properties=properties
    )

    interval_minutes: int = int(os.environ["DUPDATER_INTERVAL_IN_MINUTES"])
    schedule.every(interval_minutes).minutes.do(app.update)

    logging.info("The application is running...")
    while True:
        schedule.run_pending()
        time.sleep(1)
