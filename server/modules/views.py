from base64 import b64encode, b64decode
import re
from glob import glob

from django.http import JsonResponse, HttpRequest, FileResponse


def modules_list_files(request: HttpRequest):
    module_name = re.sub("/api/module/|/client", "", request.path)
    files = []
    for file in glob("server/modules/src/" + module_name + "/client/*"):
        file = file.replace("\\", "/").replace("server/modules/src/" + module_name + "/client/", "")
        files.append(b64encode(file.encode('ascii')).decode('ascii'))
    return JsonResponse(files, safe=False)


def module_get_file(request: HttpRequest, file: str):
    module_name = re.sub("/api/module/|/client/[a-zA-Z0-9=]+", "", request.path)
    file_name = b64decode(file.encode('ascii')).decode('ascii')

    file = open("server/modules/src/" + module_name + "/client/" + file_name, 'rb')
    return FileResponse(file)
