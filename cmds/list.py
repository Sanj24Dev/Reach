from os import *
import time

def cumtom_command_function():
    cwd = getcwd()
    system('ls ' + cwd)

cumtom_command_function()