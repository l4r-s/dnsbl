import os
import sys
import subprocess

all_hosts_file = 'data/all-hosts.txt'
unbound_hosts_file = 'data/unbound.conf'
dnsmasq_hosts_file = 'data/dnsmasq.conf'
hosts_file = 'data/hosts'

##
# helpers
##
def is_whitelist(domain):
    whitelist = False

    if os.path.exists('whitelist.txt'):
        f = open('whitelist.txt', 'r')
        for l in f.readlines():
            if domain.rstrip('\n') == l.rstrip('\n'):
                whitelist = True
                break
        f.close()

    return whitelist

##
# remove previous files
##
for f in os.listdir('data/'):
    os.remove('data/' + f)

##
# get all sources
##
process_list = []
for script in os.listdir('sources'):
    process_list.append({ 'script': script, 'proc': subprocess.Popen([ 'venv/bin/python', 'sources/' + script ]) })

# wait for all sources to finish
script_failed = False
for p in process_list:
    p['proc'].wait()

    if p['proc'].returncode != 0:
        print('ERROR - script {} failed!'.format(p['script']))
        script_failed = True

##
# uniq hosts.txt file
##
if os.path.exists(all_hosts_file):
    os.remove(all_hosts_file)

domain_set = set()
for hf in os.listdir('data'):
    if '-hosts.txt' not in hf:
        continue

    f = open('data/' + hf, 'r')

    for l in f.readlines():
        if not is_whitelist(l):
            if l.rstrip('\n') not in domain_set:
                domain_set.add(l.rstrip('\n'))
    f.close()

f_all = open(all_hosts_file, 'a')
for l in sorted(domain_set):
    if l.startswith('#') or l.startswith('(') or len(l) == 0:
        continue

    f_all.write(l.rstrip('\n') + '\n')

f_all.close()

##
# hosts config files
##
if os.path.exists(unbound_hosts_file):
    os.remove(unbound_hosts_file)

if os.path.exists(dnsmasq_hosts_file):
    os.remove(dnsmasq_hosts_file)

if os.path.exists(hosts_file):
    os.remove(hosts_file)

all_hosts = open(all_hosts_file, 'r')
hosts = open(hosts_file, 'a')
dnsmasq = open(dnsmasq_hosts_file, 'a')
unbound = open(unbound_hosts_file, 'a')

unbound.write('server:\n')

for l in all_hosts.readlines():
    domain = l.rstrip('\n')

    unbound.write('local-data: "{} A 0.0.0.0"\n'.format(domain))
    unbound.write('local-data: "{} AAAA ::"\n'.format(domain))

    dnsmasq.write('server=/{}/0.0.0.0\n'.format(domain))
    dnsmasq.write('server=/{}/::\n'.format(domain))

    hosts.write('0.0.0.0 {}\n'.format(domain))
    hosts.write(':: {}\n'.format(domain))

unbound.close()
hosts.close()

if script_failed:
    sys.exit(1)

sys.exit(0)
