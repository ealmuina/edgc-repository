import hashlib

from flask import abort

from model import Task, Domain


def classify_domain(domain):
    # TODO Make it real
    return 2, 2, 2  # cpu_intensity, com_intensity, io_intensity


def get_task(domain_id):
    try:
        domain = Domain.get_by_id(domain_id)
        cpu_intensity, com_intensity, io_intensity = classify_domain(domain)
        task = Task.get(
            ~Task.completed,
            Task.domain.is_null(),
            Task.cpu_intensity <= cpu_intensity,
            Task.com_intensity <= com_intensity,
            Task.io_intensity <= io_intensity
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
        'cpu_intensity': task.cpu_intensity,
        'com_intensity': task.com_intensity,
        'io_intensity': task.io_intensity,
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
