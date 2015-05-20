import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    old_key = None
    old_value = 0
    counter = 0
    
    for line in sys.stdin:
        data = line.strip().split("\t")
        
        if len(data) != 2:
            continue
            
        this_key, this_value = data
        if old_key and old_key != this_key:
            print_result(old_key, old_value/counter)
            old_value = 0
            counter = 0
            
        old_key = this_key
        old_value += float(this_value)
        counter += 1
        
    if old_key != None:
        print_result(old_key, old_value/counter)
        
def print_result(key, value):
    print "{0}\t{1}".format(key, value)

mapper()