#!/bin/env python

# Create a dict from the config file
with open('Systems') as fo:
    uucp_system_names = { splitline[0]: splitline[4] for splitline in [ line.split() for line in fo.readlines()]
                          if splitline[4] != '-' }

print( uucp_system_names)

for servername in ['rochester', 'leicester']:
    print( uucp_system_names.get(servername, servername))