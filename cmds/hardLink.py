import os
import sys
 
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