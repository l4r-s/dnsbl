import os
import sys
import subprocess

all_hosts_file = 'all-hosts.txt'
unbound_hosts_file = 'unbound.conf'
hosts_file = 'hosts'

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

def add_uniq_line(line, filepath):
    exists = False

    if os.path.exists(filepath):
        f = open(filepath, 'r')

        for l in f.readlines():
            if line == l:
                exists = True
                break
        f.close()

    if not exists:
        f = open(filepath, 'a')
        f.write(line)
        f.close()

##
# get all sources
##
process_list = []
for script in os.listdir('sources'):
    process_list.append({ 'script': script, 'proc': subprocess.Popen([ 'python', 'sources/' + script ]) })

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

for hf in os.listdir('data'):
    f = open('data/' + hf, 'r')
    for l in f.readlines():
        if not is_whitelist(l):
            add_uniq_line(l, all_hosts_file)

    f.close()

##
# unbound and traditional hosts file
##
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

if script_failed:
    sys.exit(1)

sys.exit(0)
