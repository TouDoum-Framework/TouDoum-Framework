import os
import requests


class Api:
    url: str
    token: str

    def __init__(self):
        self.url = os.environ.get('API_URL')
        self.token = os.environ.get('TOKEN_USER_CONTENT')

    def url_search_builder(self, path: str, filter_content: dict) -> str:
        url = self.url
        if not url.endswith('/') and not path.startswith('/'):
            url += '/'
        url += path

        if filter_content is not None:
            url += "?"

            for name, content in filter_content.items():
                url += name + "=" + content + "&"

            if url.endswith("&"):
                url = url[:-1]

        return url

    def get_client_file(self, module_name):
        url = self.url_search_builder("file/", {
            "module": module_name,
            "client": "1"
        })
        reply = requests.get(url, headers=self.get_authorization_headers())
        if reply.status_code == 200:
            path = "client/modules/" + module_name
            if not os.path.exists(path):
                os.makedirs(path)

            for file in reply.json()['results']:
                pass

        else:
            print("Error for task " + module_name + ": " + str(reply.status_code))

    def get_authorization_headers(self):
        token = "Token " + self.token
        return {'Authorization': token}
