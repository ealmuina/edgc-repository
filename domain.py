from antlr4 import *
from flask import request

from model import Domain
from parsing.CPUinfoLexer import CPUinfoLexer
from parsing.CPUinfoParser import CPUinfoParser
from parsing.cpuinfo import Evaluator


def register(domain):
    ip_addr = request.remote_addr
    nodes = len(domain)
    cpus = 0

    for node in domain:
        # Parse cpuinfo file
        cpuinfo = InputStream(node['cpuinfo'])
        lexer = CPUinfoLexer(cpuinfo)
        stream = CommonTokenStream(lexer)
        parser = CPUinfoParser(stream)
        tree = parser.compileUnit()

        # Evaluate cpuinfo content
        evaluator = Evaluator()
        processors = evaluator.visit(tree)

        # Update domain global information
        cpus += len(processors)

    try:
        domain = Domain.get(ip=ip_addr)
    except Domain.DoesNotExist:
        domain = Domain(ip=ip_addr)

    domain.nodes = nodes
    domain.cpus = cpus
    domain.save()

    return {
        "id": domain.get_id()
    }
