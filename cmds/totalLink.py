import os
import sys
from os import *
 
# Source file path
cwd = getcwd()
a = '//mnt//d//sem5//osproj//Reach//level0//level1//a.txt'
b = '//mnt//d//sem5//osproj//Reach//level0//level1//b.txt'
rela = os.path.relpath(a,cwd)
relb = os.path.relpath(b,cwd)

n = os.stat(rela).st_nlink + os.stat(relb).st_nlink 
print("Total links : ")
print(n)