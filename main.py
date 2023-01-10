from os import *
import os
import time


commands = [
    "play",
    "begin",
    "scroll",
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

    # change the projDir variable to hold the path of the game directory
    projDir = '//mnt//d//sem5//osproj//Reach'


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
            path = projDir + '//cmds//show.py'
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
                    print("  Yaay!! You've reached the fort. Game over\n\n\n")
                    quit()

        elif(input_arr[0] == commands[4]): # open
            path = projDir + '//cmds//open.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1])

        elif(input_arr[0] == commands[5]):  # list
            path = projDir + '//cmds//list.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel)

        elif(input_arr[0] == commands[6]): #num
            path = projDir + '//cmds//numChar.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1])

        elif(input_arr[0] == commands[7]): #real
            path = projDir + '//cmds//hardLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1] + " " + input_arr[2] + " " + projDir)

        elif(input_arr[0] == commands[8]): #img
            path = projDir + '//cmds//softLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1] + " " + input_arr[2] + " " + projDir)

        elif(input_arr[0] == commands[9]): #remove
            path = projDir + '//cmds//removeLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1])

        elif(input_arr[0] == commands[10]): #total
            path = projDir + '//cmds//totalLink.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + projDir)

        elif(input_arr[0] == commands[11]): #build
            path = projDir + '//cmds//build.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel)

        elif(input_arr[0] == commands[12]): #check
            path = projDir + '//cmds//check.py'
            rel = os.path.relpath(path,cwd)
            system('python3 ' + rel + " " + input_arr[1])

        elif(input_arr[0] == commands[13]): #quit
            quit()

        else:
            print("Oops! It is a wrong command. Type the correct command.")
shell()