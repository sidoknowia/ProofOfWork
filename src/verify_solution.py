import hashlib, string, random
from helpers import readFile, writeFile

class Verify:
    def __init__(self, input_txt_path, target_txt_path, solution_path_text):
        m = " ".join(readFile(input_txt_path))
        t = " ".join(readFile(target_txt_path))
        s = " ".join(readFile(solution_path_text))

        ver = self.validateSol(s, m, t)
        #return ver


    def validateSol(self,s, m, t):
        # sha = hashlib.sha256()
        tempStr = m + str(s)
        # tempStr = tempStr.encode()
        # sha.update(tempStr)
        # hash_op = sha.hexdigest()

        hash_op = hashlib.sha3_256(tempStr.encode('utf-8')).hexdigest()
        #print(tempStr, hash_op)

        h_op = int(hash_op, 16)
        t_op = int(t, 2)

        if h_op <= t_op:
            print(1)
            return 1
        else:
            print(0)
            return 0