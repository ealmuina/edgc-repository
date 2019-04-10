import hashlib

from flask import abort

from model import Task, Domain


def get_task(domain_id):
    # TODO Make it real
    try:
        domain = Domain.get_by_id(domain_id)
        task = Task.get_or_create(
            domain=domain,
            kernel='kernel/kernel-0.txt',
            input='input/in-0.tar.gz'
        )
        task.output = None
        task.completed = False
        task.save()
        return task
    except Domain.DoesNotExist:
        abort(404)


def md5(file_name):
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Create a handler for our read (GET) task
def read(domainId):
    print(f'Node {domainId} requested task')
    task = get_task(domainId)
    # Return task metadata
    return {
        'id': 1,
        'kernel': task.kernel,
        'input': task.data,
        'kernel_md5': md5(task.kernel),
        'input_md5': md5(task.data)
    }


def report(taskId):
    try:
        task = Task.get_by_id(taskId)

    except Task.DoesNotExist:
        abort(404)
