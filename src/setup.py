#!/usr/bin/env python


import os
import sys

main_dir = r"C:\Users\ydava\gestures\src"
modules = [
    r"utils",
    r"dataCollection",
    r"gym"
]
for module in modules:
    mymodule_dir = os.path.join( main_dir, module )
    sys.path.append( mymodule_dir )
