#!/usr/bin/env python

# Import regex
import os
import re

# Source and Target List
source = 'index.html'
targets = [l for l in os.listdir('.') if '.html' in l and  l != 'index.html']

# Tags we will split on
tags = ['<!-- Header -->','<!-- Footer -->','<!-- Sponsors -->']

# Go through targets and replace
for target in targets:

    # Open Targets and Files
    with open(source,'r') as f: s = f.read()
    f = open(target,'r+')
    t = f.read()
    
    # Iterate over Tags
    for tag in tags:

        if tag not in t: continue

        # Replace
        t = t.split(tag)
        t[1] = s.split(tag)[1] 

        # Join back p
        t = tag.join(t)

    f.seek(0) # Go to start of file
    f.write(t) # Write to file
    f.truncate() # Get rid of the rest
    f.close()