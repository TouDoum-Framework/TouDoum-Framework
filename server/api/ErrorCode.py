from django.http import JsonResponse


def badMethod():
    return JsonResponse({"error": "bad method used"}, safe=False, status=400)


def NoneConfigExist():
    return JsonResponse({"error": "no config exist"}, safe=False, status=501)


def PluginDoesNotExist():
    return JsonResponse({"error": "plugin does not exist"}, safe=False, status=404)
