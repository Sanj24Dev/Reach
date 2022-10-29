from os import *
import sys

def cumtom_command_function():
    opt = sys.argv[1]
    if opt == "a":
        processes = 5
        resources = 4
        max_resources = [8,5,9,7]
        currently_allocated = [[2,0,1,1],[0,1,2,1],[4,0,0,3],[0,2,1,0],[1,0,3,0]]
        max_need = [[3,2,1,4],[0,2,5,2],[5,1,0,5],[1,5,3,0],[3,0,3,3]]
    elif opt == "b":
        processes = 5
        resources = 3
        max_resources = [3,3,2]
        currently_allocated = [[0,1,0],[1,0,0],[1,0,1],[0,1,1],[1,1,0]]
        max_need = [[7,5,3],[3,2,3],[4,2,5],[7,3,2],[2,3,2]]
    elif opt == "c":
        processes = 4
        resources = 3
        max_resources = [10, 5,7]
        currently_allocated = [[0,1,0],[2,0,0],[3,0,2],[2,1,1]]
        max_need = [[7,5,3],[3,2,2],[9,0,2],[2,2,2]]

    allocated = [0] * resources
    for i in range(processes):
        for j in range(resources):
            allocated[j] += currently_allocated[i][j]
    print(f"\ntotal allocated resources : {allocated}")

    available = [max_resources[i] - allocated[i] for i in range(resources)]
    print(f"total available resources : {available}\n")

    running = [True] * processes
    count = processes
    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"Check door {i + 1}")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("Door doesnt open")
            break

        print(f" Door opened\n")

cumtom_command_function()