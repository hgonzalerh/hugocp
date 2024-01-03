#!/bin/env python
'''
hugocp, an implementation of some of the uucp command, using scp as a back end

All auth setup should be done outside the utility
Usage:
uucp <local file> <remote server>!<remote path>
'''
import subprocess
import argparse
import re

# Default configuration

system_config_file = '/etc/uucp/Systems'

# Create a dict from the config file
with open(system_config_file) as fo:
    # Field 0 is UUCP server name, field 4 is a hostname or an ip address
    uucp_system_names = { splitline[0]: splitline[4] for splitline in [ line.split() for line in fo.readlines()]
                          if splitline[4] != '-' }

def scan_spool_dir(source_file):
    ''' Scan the whole spool dir and initiate transfers. If source_file is included, 
    initiate only one trasfer for it'''
    with controlfile as open(source_file + '.control', 'r'):
        scp_cli = controlfile.read().strip()
    subprocess.run(f"scp {spool_dir}/{source_file} {scp_cli}")


#  if -r option is not present, don't scan the spool dir

commandline = "uucp -r inputfile destination_server!user:/destination/full/path"

destination_spec = "destination_server!user:/destination/full/path"

# Group 2 is always the user name and will not get captured if there isn't one
destination_regex = r'([._\w]+)!([._\w]+:)?([/-.\w]+)'

def enqueue_transfer(source_file, destination_path):
    """Create a control file and copy both the tx file and the control to the spool dir"""
    with controlfile as open(source_file + '.control', 'w'):
        controlfile.write(destination_path)


