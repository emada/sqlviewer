from vizydrop.sdk.application import Application
from .auth import NoAuth
from .source import PostgresSource


class Postgres(Application):
    class Meta:
        version = "1.0"
        name = "Postgres Connector"
        website = "http://www.fantasticatecnologia.com.br/"
        color = "#FF9900"
        description = "Postgres connector for the Vizydrop Python SDK."
        tags = ['postgres', 'api']

        authentication = [NoAuth, ]

        sources = [PostgresSource, ]
