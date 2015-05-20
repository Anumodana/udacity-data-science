import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    max_entries = 0
    old_key = None
    datetime = ''

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 4:
            continue
            
        this_key, this_entries_hourly, this_date, this_time = data
        this_entries_hourly = float(this_entries_hourly)
        if old_key and old_key != this_key:
            print_result(old_key, datetime, max_entries)
            max_entries = 0
            datetime = ''
                
        old_key = this_key
        if this_entries_hourly >= max_entries:
            max_entries = this_entries_hourly
            datetime = "{0} {1}".format(this_date, this_time)
            
    if old_key != None:
        print_result(old_key, datetime, max_entries)
            
def print_result(key, datetime, max_entries):
    print "{0}\t{1}\t{2}".format(key, datetime, max_entries)

reducer()

