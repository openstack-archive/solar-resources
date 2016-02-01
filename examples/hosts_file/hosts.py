#!/usr/bin/python
from solar.core.resource import resource as rs


def run():

    node1, node2 = rs.load_all(startswith='node')[:2]
    hosts1, hosts2 = rs.load_all(startswith='hosts_file')[:2]

    node1.connect(hosts1, {
        'name': 'hosts:name',
        'ip': 'hosts:ip',
    })

    node2.connect(hosts1, {
        'name': 'hosts:name',
        'ip': 'hosts:ip',
    })

    node1.connect(hosts2, {
        'name': 'hosts:name',
        'ip': 'hosts:ip',
    })

    node2.connect(hosts2, {
        'name': 'hosts:name',
        'ip': 'hosts:ip',
    })

run()
