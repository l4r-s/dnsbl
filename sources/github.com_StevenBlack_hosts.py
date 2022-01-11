import os
import sys
import requests

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from utils import *

url = 'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts'

file_name = os.path.basename(__file__)
hosts_file = os.path.join(sys.path[0], '../data/' + file_name.replace('.py','') + '-hosts.txt')

r = requests.get(url)
if not r.ok:
    print('ERROR - failed to get URL {}'.format(url))
    sys.exit(1)

if os.path.exists(hosts_file):
    os.remove(hosts_file)

local_part = True
for line in r.iter_lines():
    s = line.decode("utf-8")

    if local_part:
        if s == '# End of custom host records.':
            local_part = False

        continue

    if s.startswith('#') or s == '':
        continue

    add_uniq_line(s.split('\t')[-1] + '\n', hosts_file)

sys.exit(0)
