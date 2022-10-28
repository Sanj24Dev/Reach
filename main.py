from os import *
import os
import time


commands = [
    "reach",
    "begin",
    "show",
    "push",
    "open",
    "list",
    "numChar",

    "hardLink",
    "softLink",
    "removeLink",
    "totalLink"
]

def shell():

    """
    Function that runs the game.

    """
    


    startup = 1
    from_cmd_error = 0
    level = 0  #incremented in push function
    while 1:
        if startup == 1:
            startup = startup + 1
            _ = system('clear')
            userinput = input("Reach@user/Level"+str(level)+" : ")
            input_arr = userinput.split()
            if(input_arr[0]==commands[0]):
                chdir('level0')
                system('cat readme.txt')
            
            
            # shell_help()        
        
        if (from_cmd_error == 0):
            userinput = input("Reach@user/Level"+str(level)+" : ")
            pass
        
        input_arr = userinput.split()
        cwd = getcwd()
        # print(cwd)
        if(input_arr[0] == commands[1]):# begin
            # pipe for IPC 
            #path = "mypipe"
            #mode = 0o777
            #os.mkfifo(path)

            chdir('level1')
            level = 1

        elif(input_arr[0] == commands[2]): # show
            path = '//mnt//d//sem5//osproj//Reach//cmds//show.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel)
        elif(input_arr[0] == commands[3]): # push
            # with open("mypipe", "w") as f:
                # f.write(input_arr[1])
            level = level + 1
            lev = 'level'+str(level)
            chdir(lev)
        elif(input_arr[0] == commands[4]): # open
            path = '//mnt//d//sem5//osproj//Reach//cmds//open.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1])
        elif(input_arr[0] == commands[5]):  # list
            path = '//mnt//d//sem5//osproj//Reach//cmds//list.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel)
        elif(input_arr[0] == commands[6]): #num
            path = '//mnt//d//sem5//osproj//Reach//cmds//numChar.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1])
        elif(input_arr[0] == commands[7]): #hardlink
            path = '//mnt//d//sem5//osproj//Reach//cmds//hardLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1] + " " + input_arr[2])
        elif(input_arr[0] == commands[8]): #softlink
            path = '//mnt//d//sem5//osproj//Reach//cmds//softLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1] + " " + input_arr[2])
        elif(input_arr[0] == commands[9]): #removeLink
            path = '//mnt//d//sem5//osproj//Reach//cmds//removeLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1])
        elif(input_arr[0] == commands[10]): #total
            path = '//mnt//d//sem5//osproj//Reach//cmds//totalLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel)
shell()