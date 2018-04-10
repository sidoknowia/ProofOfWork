import sys
from target_generation import Target
from solution_generation import Solution
from verify_solution import Verify
from helpers import readFile, writeFile

if __name__ == "__main__":

    args = sys.argv
    #print(args)

    if (args[1] == "target"):
        ## arg[2] - difficulty eg -2,3 etc
        ## arg[3] - target.txt - User can give name of different file. It should be in data folder


        tar = Target(args[2], args[3])

    elif (args[1] == "sol"):
        ## arg[2] - key.txt - User can give name of different file. It should be in data folder
        ## arg[3] - ciphertex.txt - User can give name of different file. It should be in data folder
        ## arg[4] - result.txt - User can give name of different file. It should be in data folder

        sol = Solution(args[2], args[3], args[4])

    elif (args[1] == "verify"):

        Verify(args[2], args[3], args[4])


    elif (args[1] == "tests"):
        writeFile("solution_list.txt", "")

        try:
            if not args[2]:
                args.append(1)
        except:
            args.append(1)

        try:
            if not args[3]:
                args.append(27)
        except:
            args.append(27)

        try:
            if not args[4]:
                args.append(False)
        except:
            args.append(False)
        print(args)


        for x in range(int(args[2]),int(args[3])):
            Target(x, "target.txt")
            Solution("input.txt","target.txt","solution.txt",bool(args[4]))


