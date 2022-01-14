from celery import shared_task

from client.core.TouDoumWorker import TouDoumWorker


@shared_task
def client_exec(module_name, function: str = None, data: dict = None):
    """
    This function can be called to register a task on rabbitmq
    :param str module_name: name of the module to be called
    :param str function: name of the function to be called (default function run on main.py is called)
    :param dict data: dict of information that can be used by the module called
    """
    # TODO on task
    # download client file if needed
    # Import it

    tdw = TouDoumWorker()
    tdw.api.get_client_file(module_name)
    print("hey " + module_name)
