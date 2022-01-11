import os
import sys
import requests

url = 'https://raw.githubusercontent.com/notracking/hosts-blocklists/master/hostnames.txt'

file_name = os.path.basename(__file__)
hosts_file = os.path.join(sys.path[0], '../data/' + file_name.replace('.py','') + '-hosts.txt')

r = requests.get(url)
if not r.ok:
    print('ERROR - failed to get URL {}'.format(url))
    sys.exit(1)

if os.path.exists(hosts_file):
    os.remove(hosts_file)

f = open(hosts_file, 'a')
for line in r.iter_lines():
    s = line.decode("utf-8")

    if s.startswith('#') or s == '':
        continue

    f.write(s.split(' ')[1] + '\n')

f.close()
sys.exit(0)
