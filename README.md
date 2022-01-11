# dnsbl generator

This repo holds an unbound and hosts file generatet list for DNS based blocking of certain hostnames/domains.

## output files

| File                         | Github             | Mirror                |
|------------------------------|--------------------|-----------------------|
| All hosts in TXT format      | [https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/all-hosts.txt](https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/all-hosts.txt) | t.b.d. |
| All hosts in hosts format    | [https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/hosts](https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/hosts) | t.b.d. |
| All hosts in unbound conf format | [https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/unbound.conf](https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/unbound.conf) | t.b.d. |
| All hosts in dnsmasq conf format | [https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/dnsmasq.conf](https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/dnsmasq.conf) | t.b.d. |
| unique hosts from StevenBlack | [https://github.com/l4r-s/dnsbl/blob/master/data/github.com_StevenBlack_hosts-hosts.txt](https://github.com/l4r-s/dnsbl/blob/master/data/github.com_StevenBlack_hosts-hosts.txt) | t.b.d. |
| unique hosts from justdomains | [https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/github.com_justdomains_blocklists-hosts.txt](https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/github.com_justdomains_blocklists-hosts.txt) | t.b.d. |
| unique hosts from notracking | [https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/github.com_notracking_hosts_blocklists-hosts.txt](https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/github.com_notracking_hosts_blocklists-hosts.txt) | t.b.d. |
| unique hosts from urlhaus.abuse.ch | [https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/urlhaus.abuse.ch-hosts.txt](https://raw.githubusercontent.com/l4r-s/dnsbl/master/data/urlhaus.abuse.ch-hosts.txt) | t.b.d. |

## sources (credit goes to!)

The following sources are used:

| Source                                      | Link                                                                            |
|---------------------------------------------|---------------------------------------------------------------------------------|
| github.com_justdomains_blocklists.py        | [https://github.com/justdomains/blocklists](https://github.com/justdomains/blocklists) |
| github.com_notracking_hosts_blocklists.py   | [https://github.com/notracking/hosts-blocklists](https://github.com/notracking/hosts-blocklists) |
| github.com_StevenBlack_hosts.py             | [https://github.com/StevenBlack/hosts](https://github.com/StevenBlack/hosts) |
| urlhaus.abuse.ch.py                         | [https://urlhaus.abuse.ch/downloads/hostfile/](https://urlhaus.abuse.ch/downloads/hostfile/) |
