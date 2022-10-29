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
os.symlink(src, dst)
 
print("Soft link created successfully\n")
print("Total links : ")
n = os.stat(src).st_nlink
print(n)

cwd = getcwd()
path = '//mnt//d//sem5//osproj//Reach//cmds//totalLink.py'
rel = os.path.relpath(path,cwd)
system('python3 ' + rel)