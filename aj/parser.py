import os
import sys

with open(sys.argv[-1], 'rb') as fp:
    for line in fp:
        line = line.strip()
        parts = line.split('\t')
        if len(parts) <= 1:
            continue
        i1, i2 = parts[:2]
        dummy, addr = i1.rsplit('.', 1)
        print '{};{}'.format(addr, i2)

