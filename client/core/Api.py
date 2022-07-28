import os
import requests

from utils.celery import reject_task
from utils.files import md5sum


class Api:
    url: str
    access: tuple
    headers: dict

    def __init__(self):
        self.url = os.environ.get('API_URL')
        self.access = (
            os.environ.get('MQ_USER', os.environ.get('USER_NAME')),
            os.environ.get('MQ_PASS', os.environ.get('USER_PASS'))
        )
        self.headers = {'Content-Type': 'application/json'}

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

    def download_client_files_for_module(self, module_name):
        url = self.url_search_builder("file/", {
            "module": module_name,
            "client": "1"
        })
        reply = requests.get(url, headers=self.get_headers(), auth=self.get_credentials())
        if reply.status_code == 200:
            path = "modules/" + module_name
            if not os.path.exists(path):
                os.makedirs(path)

            for file in reply.json()['results']:
                # check if file exists with checksum
                file_path = f"modules/{module_name}/{file['name']}"
                local_file_checksum = md5sum(file_path)
                if os.path.exists(file_path) and file['checksum'] != local_file_checksum:
                    # file exists but checksum is different
                    os.remove(file_path)
                    print(f"Removed {file_path} because checksum as changed")
                elif file['checksum'] == local_file_checksum:
                    # file exists and checksum is the same
                    print(f"File {file_path} exists and checksum is the same skipping download for this file")
                    continue

                # download file
                # override url var wee dont need latest value
                url = self.url_search_builder("file/download", {
                    "module": module_name,
                    "client": "1",
                    "checksum": file['checksum']
                })
                reply_file = requests.get(url, headers=self.get_headers(), auth=self.get_credentials())
                if reply_file.status_code == 200:
                    with open(path + "/" + file['name'], 'wb') as stream:
                        stream.write(reply_file.content)
                    print(f"File {file['name']} written on {path}")
                else:
                    reject_task(
                        reason="Error on download client files for module {}".format(module_name), requeue=True)
        else:
            reject_task(reason="Error on listing client files for module {}".format(module_name), requeue=True)

    def get_credentials(self) -> tuple:
        return self.access

    def get_headers(self) -> dict:
        return self.headers
