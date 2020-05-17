# dns-record-updater
Application for updating DNS record in auto mode. It's useful when a host has dynamic ip address and the dns records need to be updated every time when the ip is changed.

The following env variables must be set before running the application:

- DUPDATER_DOMAIN_NAME (e.g. letscode.dk)
- DUPDATER_RECORD_TYPE (e.g. A)
- DUPDATER_RECORD_NAME (e.g. web)
- DUPDATER_INTERVAL_IN_MINUTES (e.g. 10)

## Supported domain registrators

### GoDaddy

Additional env variables that must be set:

- DUPDATER_GO_DADDY_KEY
- DUPDATER_GO_DADDY_SECRET_KEY