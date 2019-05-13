import hashlib

from flask import abort

from model import Task, Domain


def get_task(domain_id):
    try:
        domain = Domain.get_by_id(domain_id)
        task = Task.get(
            ~Task.completed,
            Task.domain.is_null(),
            Task.cpu_intensity <= domain.mhz,
            Task.com_intensity <= domain.net_speed,
            Task.mem_intensity <= domain.memory
        )
        task.domain = domain
        task.save()
        return task
    except Domain.DoesNotExist:
        abort(404)
    except Task.DoesNotExist:
        abort(503)


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
        'id': task.id,
        'kernel': task.kernel,
        'input': task.input,
        'output': task.output,
        'unpack': task.unpack,
        'pack': task.pack,
        'kernel_md5': md5(task.kernel),
        'input_md5': md5(task.input),
        'unpack_md5': md5(task.unpack),
        'pack_md5': md5(task.pack)
    }


def report(domainId, taskId, outputFile):
    try:
        task = Task.get_by_id(taskId)
        # Check if task belongs to reported domain
        if task.domain.id != domainId:
            abort(404)
        outputFile.save(f'output/{outputFile.filename}')
    except Task.DoesNotExist:
        abort(404)
