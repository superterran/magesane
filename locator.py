#! /usr/bin/env python
# to provide location, for loading local resources.
# http://stackoverflow.com/questions/2632199/how-do-i-get-the-path-of-the-current-executed-file-in-python/2632297#2632297

import sys
import os


def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    return hasattr(sys, "frozen")


def module_path():
    if we_are_frozen():
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)