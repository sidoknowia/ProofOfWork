import os
##
# This file exposes certain helper functions that are repeatedly used through out the project.
##

## Helper function to read files
def readFile(path):
    if not path:
        raise ValueError('Path not defined')

    current_directory = os.path.dirname(os.path.realpath(__file__))
    #print(current_directory)
    parent_path = os.path.split(current_directory)[0]
    path = parent_path + '\\data\\' + path
    #print(path)
    f = open(path, "r")
    if f.mode == 'r':
        contents = f.read().split(" ")
        #print(contents)
    f.close()
    return contents

## Helper function to write to files
def writeFile(path, text, append = False):

    if not path:
        raise ValueError('Path not defined')

    current_directory = os.path.dirname(os.path.realpath(__file__))
    parent_path = os.path.split(current_directory)[0]
    path = parent_path + '\\data\\' + path
    #print("path : {}".format(path))

    p2 = 'w+'
    if append:
        p2 = 'a+'
        text = ",\n" + str(text)

    f = open(path,p2)

    #for i in range(12):
    f.write("{}".format(text))
    f.close()