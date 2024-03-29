#!/usr/bin/env python

import subprocess, sys

def get_stats_source():
    cmd = ['/usr/bin/docker', 'stats', '--no-stream']
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = s.communicate()
    out = out[0].split('\n')
    return out[1:]

def parse_stats(lst = get_stats_source()):
    print('len - %s' %(len(lst)), lst )
    #if len(lst) > 2:
    lst_of_dcts = []
    for i in lst[:-1]:
            #lst = ['66315a9e0        0.17%               13.65 MB / 4.147 GB   0.33%               20.42 MB / 76.06 MB   9.6 MB / 430.1 kB     0']
        src = lst[0].split(' ')
        cpu_i = 0
        for i in src:
            if '%' in i and cpu_i == 0:
                cpu = i
                cpu_i = 1
            elif '%' in i and cpu_i == 1:
                mem = i
        container_id = src[0]
        dct = {'id' : container_id, 'cpu' : cpu[:-1], 'memory' : mem[:-1]}
        lst_of_dcts.append(i)
            #print(container_id, cpu[:-1], mem[:-1])
        return lst_of_dcts



args = sys.argv
stats = parse_stats()
if len(args) > 1:
    print(stats[args[1]])
else: print(stats)
