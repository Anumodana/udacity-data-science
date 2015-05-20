import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    unit_idx = 1
    entries_hourly_idx = 6
    for line_idx, line in enumerate(sys.stdin):
        if line_idx != 0:
            data = line.strip().split(",")
            print "{0}\t{1}".format(data[unit_idx], data[entries_hourly_idx])

mapper()

