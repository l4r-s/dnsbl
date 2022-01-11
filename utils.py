import os
import subprocess

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

