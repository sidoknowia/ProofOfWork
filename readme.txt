Program - Implementation of Proof of Work
Language - Python
Version - 3.6


** Prerequisite **
User is required to install latest version of python. The program will not work in Python 2.

** Libraries **
No additional libraries have been used in this project



** File Structure **

./src/
    pow.py                      ## This is main file. User should run this file
    solution_generation.py      ## For generating the solution
    target_generation.py        ## For generating target
    verify_solution.py          ## For verifying the solution
    helpers.py                  ## helper functions that are used at several instances throughout the project
./data/
    input.txt                   ## Put your message in this file
    results.txt                 ## Result stats will be logged in this file
    solution.txt                ## Output for a particular difficulty will be logged in this file
    solution_list.txt           ## This tracks
    target.txt                  ## Target string will be kept in this list




 ** Instructions **

Open command prompt.
Change working directory to src folder for ease of implementation.

 Target Generation

    Command - python pow.py target 5 target.txt ## Do not provide full path to text files.
    parameter 1 - Asks program to target generation
    parameter 2 - Difficulty Number
    parameter 3 - Path where target needs to be saved


 Solution Generation

    Command - python pow.py sol input.txt target.txt solution.txt    ## Do not provide full path to text files.
    parameter 1 - Asks program to implement solution generation
    parameter 2 - Path to file that contains input message
    parameter 3 - Path to file that contains target string
    parameter 4 - path to file where solution is to be stored


 Verify

    Command - python pow.py verify input.txt target.txt solution.txt  ## Do not provide full path to text files.
    parameter 1 - Asks program to verify solution
    parameter 2 - Path to file that contains input message
    parameter 3 - Path to file that contains target string
    parameter 4 - path to file that contains solution


 Tests

    This allows user to test the system by rapidly running the program for different difficulty levels

    Command - python pow.py tests 1 20 True
    parameter 1 - Asks program to run multiple tests
    parameter 2 - (optional, default = 1) Minimum difficulty level
    parameter 3 - (optional, default = 27) Maximum difficulty level
    parameter 4 - (optional, default = False) This sets random mode for nounce generation

 ** Points to consider **

 - User must ensure necessary files are present in data folder, atleast before reading them
 - While running commands, do not provide entire path to text files. That will throw errors. Just provide file name
 - In test mode, parameter 3 is not inclusive ie if user provides param3 = 27, program will run for upto 26 times
 - If user wants to replicate results, he must clear contents of solution_list.txt, manually.
   However, this will be done automatically during test mode.


