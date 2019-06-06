import hashlib
from datetime import datetime

import numpy as np
from flask import abort

from model import Task, Domain

GREEDY_TASKS = True


def distance(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.linalg.norm(x - y)


def get_task(domain_id):
    try:
        domain = Domain.get_by_id(domain_id)
        tasks = Task.select().where(
            ~Task.completed,
            Task.domain.is_null(),
            Task.cpu_intensity <= domain.mflops,
            Task.com_intensity <= domain.mpi_bandwidth,
            Task.mem_intensity <= domain.memory
        )
        if GREEDY_TASKS:
            tasks = sorted(
                tasks,
                key=lambda t: distance((t.cpu_intensity, t.com_intensity, t.mem_intensity),
                                       (domain.mflops, domain.mpi_bandwidth, domain.memory))
            )
            task = tasks[0]
        else:
            task = tasks.get()
        task.domain = domain
        task.assign_date = datetime.now()
        task.save()
        return task
    except Domain.DoesNotExist:
        abort(404)
    except Task.DoesNotExist:
        abort(503)


def md5(file_name):
    if file_name:
        hash_md5 = hashlib.md5()
        with open(file_name, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    return ''


# Create a handler for our read (GET) task
def read(domainId):
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
        outputFile.save('output/%s' % outputFile.filename)
        task.completed = True
        task.completed_date = datetime.now()
        task.save()
    except Task.DoesNotExist:
        abort(404)
