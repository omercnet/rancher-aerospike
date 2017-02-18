#!/usr/bin/env python

import sys
import time
import requests
import subprocess

acceptJson = {'Accept': 'application/json'}
service = requests.get('http://rancher-metadata/2016-07-29/self/service/primary_service_name').text

while True:
    nodes = requests.get('http://rancher-metadata/2016-07-29/services/'+service+'/containers', headers=acceptJson).json()
    for host in nodes:
        for node in nodes:
            asinfo = subprocess.Popen('asinfo -h ' + host['primary_ip'] +
                                      ' -v "tip:host='+node['primary_ip']+';port=3002"', shell=True, stdout=sys.stdout)
    time.sleep(10)
