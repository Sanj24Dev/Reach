import os
import sys
from os import *
 
# Source file path
cwd = getcwd()
a = '//mnt//d//sem5//osproj//Reach//level0//level1//level2//a.txt'
b = '//mnt//d//sem5//osproj//Reach//level0//level1//level2//b.txt'
c = '//mnt//d//sem5//osproj//Reach//level0//level1//level2//c.txt'
d = '//mnt//d//sem5//osproj//Reach//level0//level1//level2//d.txt'
e = '//mnt//d//sem5//osproj//Reach//level0//level1//level2//e.txt'

rela = os.path.relpath(a,cwd)
relb = os.path.relpath(b,cwd)
relc = os.path.relpath(c,cwd)
reld = os.path.relpath(d,cwd)
rele = os.path.relpath(e,cwd)


n = os.stat(rela).st_nlink + os.stat(relb).st_nlink + os.stat(relc).st_nlink + os.stat(reld).st_nlink + os.stat(rele).st_nlink
print("Total links in the labyrinth: ")
print(n)
if n == 8:
    print("\nYayy!! You have successfully created 8 links. \nTo get out of the maze open a.txt\n")
