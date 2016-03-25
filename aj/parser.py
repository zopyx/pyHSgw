import os
import sys

with open(sys.argv[-1], 'rb') as fp:
    for line in fp:
        line = line.strip()
        parts = line.split('\t')
        if len(parts) > 1:
            print parts
