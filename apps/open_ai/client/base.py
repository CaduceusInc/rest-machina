import requests
class BaseClient(object):
    def __init__(self, api_key=None, **kwargs):
        self.api_key = api_key
        self._base_url = "https://api.openai.com/v1/"
        self._headers = {
            f"Authorization: Bearer {self.api_key}",
            "Content-Type: application/json",
        }
        self._session = None
        self.kwargs = kwargs

    def _get_session(self):
        if not self._session:
            self._session = requests.Session()
        return self._session

    def _request(self, method, url, **kwargs):
        session = self._get_session()
        return session.request(method, url, **kwargs)

    def _get(self, url, **kwargs):
        return self._request("GET", url, **kwargs)

    def _post(self, url, **kwargs):
        return self._request("POST", url, **kwargs)

    def _put(self, url, **kwargs):
        return self._request("PUT", url, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request("DELETE", url, **kwargs)

    def _patch(self, url, **kwargs):
        return self._request("PATCH", url, **kwargs)



