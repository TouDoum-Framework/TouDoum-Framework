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
    # Import it

    print("task receive for " + module_name)
    tdw = TouDoumWorker()
    tdw.api.download_client_files_for_module(module_name)
    tdw.moduleLoader.load_module(module_name)
    obj = tdw.moduleLoader.get_module_object(module_name)
    obj.run()
