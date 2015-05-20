import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    # Takes in variables indicating whether it is foggy and/or rainy and
    # returns a formatted key that you should output.  The variables passed in
    # can be booleans, ints (0 for false and 1 for true) or floats (0.0 for
    # false and 1.0 for true), but the strings '0.0' and '1.0' will not work,
    # so make sure you convert these values to an appropriate type before
    # calling the function.
    def format_key(fog, rain):
        return '{}fog-{}rain'.format(
            '' if fog else 'no',
            '' if rain else 'no'
        )
    
    entries_hourly_idx = 6
    fog_idx = 14
    rain_idx = 15
    for line_idx, line in enumerate(sys.stdin):
    	if line_idx != 0:
            data = line.strip().split(",")
            print "{0}\t{1}".format(format_key(float(data[fog_idx]), float(data[rain_idx])), data[entries_hourly_idx])

mapper()
