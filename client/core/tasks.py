from celery import shared_task


@shared_task
def client_exec(module, function: str = None, data: dict = None):
    """
    This function can be called to register a task on rabbitmq
    :param str module: name of the module to be called
    :param str function: name of the function to be called (default function run on main.py is called)
    :param dict data: dict of information that can be used by the module called
    """
    print("hey " + module)
