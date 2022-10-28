from os import *
import time
import sys

def cumtom_command_function():
    system('wc -m ' + sys.argv[1])

cumtom_command_function()