#!/usr/bin/env python

import sys
import json
import urllib2
import subprocess


q = urllib2.Request('http://rancher-metadata/2016-07-29/self/service/containers')
q.add_header('Accept', 'application/json')
nodes = json.loads(urllib2.urlopen(q).read())

heartbeat = ''
for node in nodes:
    heartbeat += '		mesh-seed-address-port '+node['primary_ip']+' 3002\n'

print 'Adding heartbeat configuration:'
print heartbeat

with open('/etc/aerospike/aerospike.conf.template', "r") as fin:
    with open('/etc/aerospike/aerospike.conf', "w") as fout:
        for line in fin:
            fout.write(line.replace('		%%HEARTBEAT%%', heartbeat))
