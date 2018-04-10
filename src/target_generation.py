import hashlib, string, random
from helpers import readFile, writeFile


class Target:

    def __init__(self, d = 2, target_txt_path = 'target.txt'):
        difficulty = int(d)
        target = "0" * difficulty + "1" * (256 - difficulty)
        print(target)
        writeFile(target_txt_path, target)

        #return target






