import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    unit_idx = 1
    entries_hourly_idx = 6
    date_idx = 2
    time_idx = 3
    for line_idx, line in enumerate(sys.stdin):
        if line_idx != 0:
            data = line.strip().split(",")
            print "{0}\t{1}\t{2}\t{3}".format(data[unit_idx], data[entries_hourly_idx], data[date_idx], data[time_idx])

mapper()

