import os
import sys
import requests

urls = [
    'https://raw.githubusercontent.com/justdomains/blocklists/master/lists/adguarddns-justdomains.txt',
    'https://raw.githubusercontent.com/justdomains/blocklists/master/lists/easylist-justdomains.txt',
    'https://raw.githubusercontent.com/justdomains/blocklists/master/lists/easyprivacy-justdomains.txt',
    'https://raw.githubusercontent.com/justdomains/blocklists/master/lists/nocoin-justdomains.txt'
]

file_name = os.path.basename(__file__)
hosts_file = os.path.join(sys.path[0], '../data/' + file_name.replace('.py','') + '-hosts.txt')

if os.path.exists(hosts_file):
    os.remove(hosts_file)

f = open(hosts_file, 'a')

for url in urls:
    r = requests.get(url)
    if not r.ok:
        print('ERROR - failed to get URL {}'.format(url))
        sys.exit(1)

    for line in r.iter_lines():
        s = line.decode("utf-8")

        if s.startswith('#') or s == '':
            continue

        f.write(s.rstrip('\n') + '\n')

f.close()
sys.exit(0)
