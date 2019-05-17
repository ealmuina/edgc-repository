from antlr4 import *
from flask import request

import parsing.cpuinfo as cpuinfo
import parsing.meminfo as meminfo
from model import Domain
from parsing.CPUinfoLexer import CPUinfoLexer
from parsing.CPUinfoParser import CPUinfoParser
from parsing.MeminfoLexer import MeminfoLexer
from parsing.MeminfoParser import MeminfoParser


def parse_file(data, parser_cls, lexer_cls, evaluator_cls):
    # Parse file
    file = InputStream(data)
    lexer = lexer_cls(file)
    stream = CommonTokenStream(lexer)
    parser = parser_cls(stream)
    tree = parser.compileUnit()

    # Evaluate content
    evaluator = evaluator_cls()
    return evaluator.visit(tree)


def register(domain):
    ip_addr = request.remote_addr
    nodes = len(domain)
    cpus = 0
    total_memory = 0
    total_bandwidth = 0
    total_mflops = 0

    for node in domain:
        # Parse cpuinfo file
        processors = parse_file(node['cpuinfo'], CPUinfoParser, CPUinfoLexer, cpuinfo.Evaluator)
        # Parse meminfo file
        memory_stats = parse_file(node['meminfo'], MeminfoParser, MeminfoLexer, meminfo.Evaluator)

        # Update domain global information
        cpus += len(processors)
        total_memory += int(memory_stats['MemTotal'].split()[0])
        total_bandwidth += float(node.get('mpi_bandwidth'))
        total_mflops += float(node.get('mflops')) * cpus

    try:
        domain = Domain.get(ip=ip_addr)
    except Domain.DoesNotExist:
        domain = Domain(ip=ip_addr)

    domain.nodes = nodes
    domain.cpus = cpus
    domain.mflops = total_mflops
    domain.mpi_bandwidth = total_bandwidth / nodes
    domain.memory = total_memory
    domain.save()

    return {
        "id": domain.get_id()
    }
