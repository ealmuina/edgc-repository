from flask import request

from model import Domain


def register(domain):
    ip_addr = request.remote_addr
    nodes = len(domain)

    try:
        domain = Domain.get(ip=ip_addr)
    except Domain.DoesNotExist:
        domain = Domain(ip=ip_addr)

    domain.nodes = nodes
    domain.save()

    return {
        "id": domain.get_id()
    }
