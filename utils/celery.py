from celery.exceptions import Reject


def reject_task(reason="Error Undefined", requeue=True) -> None:
    """
    Rejects the task to rabbitmq.
    :param reason: Message to be displayed in the logs.
    :param requeue: Can the task be requeued?
    """
    print(f"Task rejected: {reason}")
    raise Reject(reason=reason, requeue=requeue)
