import time

from solar.core.resource import composer as cr
from solar.core.resource import resource as rs
from solar import errors
from solar.dblayer.model import ModelMeta
from solar.core.transports.base import locate_named_transport_resoruce


def run():
    node1 = rs.load_all(startswith='node')[0]
    hosts1 = rs.load_all(startswith='hosts_file')[0]
    # let's add torrent transport for hosts file deployment (useless in real life)

    torrent_transport = cr.create('torrent_transport',
                                  'resources/transport_torrent',
                                  {'trackers': ['udp://open.demonii.com:1337',
                                                'udp://tracker.openbittorrent.com:80']})[0]
    # you could use any trackers as you want

    transports_for_torrent = cr.create(
        'transports_for_torrent', 'resources/transports')[0]

    transports_for_torrent.connect(torrent_transport, {})

    ssh_transport = locate_named_transport_resoruce(node1, 'ssh')

    ssh_transport.connect_with_events(transports_for_torrent, {'key': 'transports:key',
                                                               'password': 'transports:password',
                                                               'user': 'transports:user',
                                                               'port': 'transports:port',
                                                               'name': 'transports:name'},
                                      events={})

    transports_for_hosts = cr.create(
        'transports_for_hosts', 'resources/transports')[0]

    torrent_transport.connect(transports_for_hosts, {'trackers': 'transports:trackers',
                                                     'name': 'transports:name'})

    ssh_transport.connect(transports_for_hosts, {'key': 'transports:key',
                                                 'password': 'transports:password',
                                                 'user': 'transports:user',
                                                 'port': 'transports:port',
                                                 'name': 'transports:name'})

    transports_for_hosts.connect(hosts1)
    transports_for_hosts.connect_with_events(node1, events={})

    node1.connect(hosts1, {
        'ip': 'hosts:ip',
        'name': 'hosts:name'
    })

run()
