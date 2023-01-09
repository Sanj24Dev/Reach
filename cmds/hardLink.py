import os
import sys
from os import *

 
# Source file path
src = sys.argv[1]
 
# Destination file path
dst = sys.argv[2]
 
# Create a hard link
# pointing to src named dst
# using os.link() method
os.link(src, dst)
 
print("Hard link created successfully\n")
print("Total links : ")
n = os.stat(src).st_nlink
print(n)

cwd = getcwd()
path = sys.argv[3] + '//cmds//totalLink.py'
rel = os.path.relpath(path,cwd)
system('python3 ' + rel + " " + sys.argv[3])