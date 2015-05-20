import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    old_key = None
    old_value = 0
    
    for line in sys.stdin:
        data = line.strip().split("\t")
        
        if len(data) != 2:
            continue
            
        this_key, this_value = data
        if old_key and old_key != this_key:
            print_result(old_key, old_value)
            old_value = 0
            
        old_key = this_key
        old_value += float(this_value)
        
    if old_key != None:
        print_result(old_key, old_value)

def print_result(key, value):
    print "{0}\t{1}".format(key, value)
        
reducer()
