import os
import subprocess
from utils import *

all_hosts_file = 'data/all-hosts.txt'
unbound_hosts_file = 'data/unbound.txt'
hosts_file = 'data/hosts.txt'

# get all sources
process_list = []
for script in os.listdir('sources'):
    process_list.append({ 'script': script, 'proc': subprocess.Popen([ 'python', 'sources/' + script ]) })

# wait for all sources to finish
for p in process_list:
    p['proc'].wait()

    if p['proc'].returncode != 0:
        print('ERROR - script {} failed!'.format(p['script']))

# create uniq hosts.txt file
if os.path.exists(all_hosts_file):
    os.remove(all_hosts_file)

for hf in os.listdir('data'):
    if '-hosts' not in hf:
        continue

    f = open('data/' + hf, 'r')
    for l in f.readlines():
        if not is_whitelist(l):
            add_uniq_line(l, all_hosts_file)

    f.close()

# create unbound and traditional hosts file
if os.path.exists(unbound_hosts_file):
    os.remove(unbound_hosts_file)

if os.path.exists(hosts_file):
    os.remove(hosts_file)

all_hosts = open(all_hosts_file, 'r')
hosts = open(hosts_file, 'a')
unbound = open(unbound_hosts_file, 'a')
unbound.write('server:\n')

for l in all_hosts.readlines():
    domain = l.rstrip('\n')

    unbound.write('local-data: "{} A 0.0.0.0"\n'.format(domain))
    unbound.write('local-data: "{} AAAA ::"\n'.format(domain))

    hosts.write('0.0.0.0 {}\n'.format(domain))
    hosts.write(':: {}\n'.format(domain))

unbound.close()
hosts.close()

