from tornado.httpclient import HTTPRequest
from tornado import gen

from vizydrop.sdk.account import Account


class NoAuth(Account):
    class Meta:
        identifier = 'none'
        name = "No Auth"
        description = "No Authentication Necessary"

    def get_request(self, url, **kwargs):
        return HTTPRequest(url, **kwargs)

    @gen.coroutine
    def validate(self):
        return "No Authentication Needed"

    def get_friendly_name(self):
        return "Vizydrop Postgres Connector"
