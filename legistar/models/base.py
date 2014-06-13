import requests


class LegistarODataBase(object):
    LEGISTAR_API_ROOT = "http://webapi.legistar.com/v1"
    DEBUG = False

    def __init__(self, legistar_client, debug=False):
        self.legistar_client = legistar_client
        self.DEBUG = debug

    def request(self, method, url, params=None, data=None):
        url = "%s/%s/%s" % (
            self.LEGISTAR_API_ROOT,
            self.legistar_client,
            url,
        )
        return requests.request(
            method,
            url,
            params=params,
            data=data,
            headers={"Accept": "application/json"}
        ).json()
