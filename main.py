from os import *
import os
import time


commands = [
    "play",
    "begin",
    "show",
    "push",
    "open",
    "list",
    "num",

    "real",
    "img",
    "remove",
    "total",

    "build",
    "check",

    "quit"
]

h=0
l=0

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
            userinput = input("\nReach@user/Level"+str(level)+" : ")
            input_arr = userinput.split()
            if(input_arr[0]==commands[0]): #play
                chdir('level0')
                system('cat readme')
            
            # creating a pipe for saving the clues for final level
            r, w = os.pipe()
            
            # shell_help()        
        
        if (from_cmd_error == 0):
            userinput = input("\nReach@user/Level"+str(level)+" : ")
            pass
        
        input_arr = userinput.split()
        cwd = getcwd()
        # print(cwd)
        if(input_arr[0] == commands[1]):# begin           
            chdir('level1')
            level = 1

        elif(input_arr[0] == commands[2]): # show
            path = '//mnt//d//sem5//osproj//Reach//cmds//show.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel)

        elif(input_arr[0] == commands[3]): # push
            c = input_arr[1]
            if level == 1 and c != "F":
                print("Wrong letter!! Try again")
                # continue
            elif level == 2 and c != "O":
                print("Wrong letter!! Try again")
                # continue
            elif level == 3 and c != "R":
                print("Wrong letter!! Try again")
                # continue
            elif level == 4 and c != "T":
                print("Wrong letter!! Try again")
                # continue
            else:
                c = c.encode("ascii")
                os.write(w,c)
                level = level + 1
                lev = 'level'+str(level)
                _ = system('clear')
                chdir(lev)
                if level == 5:
                    os.close(w)
                    r = os.fdopen(r)
                    print("\n\n\n  FINAL answer ", r.read())
                    print("  Game over")
                    quit()

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

        elif(input_arr[0] == commands[7]): #real
            h=h+1
            path = '//mnt//d//sem5//osproj//Reach//cmds//hardLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1] + " " + input_arr[2] + " " + h)

        elif(input_arr[0] == commands[8]): #img
            l=l+1
            path = '//mnt//d//sem5//osproj//Reach//cmds//softLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1] + " " + input_arr[2] + " " + l)

        elif(input_arr[0] == commands[9]): #remove
            path = '//mnt//d//sem5//osproj//Reach//cmds//removeLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1])

        elif(input_arr[0] == commands[10]): #total
            path = '//mnt//d//sem5//osproj//Reach//cmds//totalLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel)

        elif(input_arr[0] == commands[11]): #build
            path = '//mnt//d//sem5//osproj//Reach//cmds//build.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel)

        elif(input_arr[0] == commands[12]): #check
            path = '//mnt//d//sem5//osproj//Reach//cmds//check.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1])

        elif(input_arr[0] == commands[13]): #quit
            quit()

        else:
            print("Oops! It is a wrong command. Type the correct command.")
shell()