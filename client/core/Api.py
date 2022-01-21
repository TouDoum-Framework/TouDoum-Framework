import os
import requests


class Api:
    url: str
    token: str

    def __init__(self):
        self.url = os.environ.get('API_URL')
        self.token = os.environ.get('TOKEN')

    def get_module_configuration(self, module_name):
        reply = requests.get(self.url + "/module/?name=" + module_name, headers=self.get_authorization_headers())

    def get_client_file(self, module_id):
        pass

    def get_authorization_headers(self):
        return {'Authorization': 'Token ' + self.token}


        return url

    def get_client_file(self, module_name):
        url = self.url_search_builder("file/", {
            "module": module_name,
            "client": "1"
        })
        reply = requests.get(url, headers=self.get_authorization_headers())
        pass

    def get_authorization_headers(self):
        return {'Authorization': 'Token ' + self.token}
