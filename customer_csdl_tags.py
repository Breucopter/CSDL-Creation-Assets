#!/usr/bin/python

# CSV to CSDL tags social profiling script
#	Justin @ DataSift
#
# Usage: profiling_script.py [customer_ids].csv [new_file].txt

# The format of the .csv file needs to be [customer id] [twitter.user.id] [facebook.author.id]
# This script is fully extensible and future iterations will allow for the targets to be
# automatically generated based on the headers.

import csv
import sys

if len(sys.argv) != 3:
    print "Usage:$ profiling_script.py [customer_ids].csv [new_file].txt"
    sys.exit("please follow proper function usage")
    pass

customer_ids = open(sys.path[0]+'/'+sys.argv[1],'U')
csv_reader = csv.reader(customer_ids)
CSDL_output = open(sys.path[0]+'/'+sys.argv[2],'w')

for counter,row in enumerate(csv_reader):
	if counter == 0:
		header_keys = []
		for i,value in enumerate(row):
			header_keys.insert(i,value)
			continue
		continue
	if counter >= 1:
		CSDL_output.write("tag.customer_id \"" + row[0] + "\" {twitter.user.id in [" + row[1] + "] OR twitter.retweet.user.id in [" + row[1] + "] OR facebook.author.id in \"" + row[2] + "\"}\n")
	else:
		continue
