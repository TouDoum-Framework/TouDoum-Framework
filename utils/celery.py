from celery.exceptions import Reject


def reject_task(reason="Error Undefined", requeue=True):
    print(f"Task rejected: {reason}")
    raise Reject(reason=reason, requeue=requeue)
