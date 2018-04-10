import hashlib, time,random,string
from helpers import readFile, writeFile

class Solution:

    def __init__(self, input_txt_path, target_txt_path, solution_path_text,random_mode=False):
        m = " ".join(readFile(input_txt_path))
        t = " ".join(readFile(target_txt_path))

        self.rand_mode = random_mode

        self.start_time = time.time()
        self.solution_list = readFile("solution_list.txt")

        if '' in self.solution_list:
            self.solution_list.remove('')

        print(self.solution_list)
        sol,diff,hash_sol,num_hashes = self.testSol(m, t)


        time_taken = time.time() - self.start_time

        print("Time taken :", time_taken)
        writeFile(solution_path_text, sol)

        temp_str = " ".join([x for x in self.solution_list])
        #temp_str = temp_str[1:]
        writeFile("solution_list.txt", temp_str)

        results = {
            "message": m,
            "solution": sol,
            "difficulty": diff,
            "hash": hash_sol,
            "time_taken": time_taken,
            "num_of_hashes": num_hashes
        }

        writeFile("results.txt", results, True)

    def generation(self, msg, a=0):
        if self.rand_mode:
            ans = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(5))
        else:
            ans = ''

        ans += str(a)
        at = msg + str(ans)
        if a % 1000000 == 0:
            print(at)
        return at, ans

    def testSol(self, m ,t):
        found = False
        i = 0
        ans = 0

        diff = 0
        for x in str(t):
            if x == "0":
                diff += 1
            else:
                break

        t_op = int(t, 2)
        print(t_op)



        while found == False:
            s, a = self.generation(m, i)

            hash_op = hashlib.sha3_256(s.encode('utf-8')).hexdigest()

            #hash_op = codecs.decode(hash_op, 'hex_codec') #bytes.fromhex(hash_op) #str(hash_op).decode('hex') #bytearray.fromhex(hash_op)

            # sha1 = hashlib.sha256()
            # t1 = str(t).encode()
            # sha1.update(t1)
            t_hash = hashlib.sha3_256(t.encode('utf-8')).hexdigest() #sha1.hexdigest()

            #print(type(hash_op), type(t))
            #print(int(hash_op,16) - int(t,2))
            #print(codecs.decode(hash_op, 'hex_codec') - codecs.decode(t, 'hex_codec'))

            h_op = int(hash_op,16)

            if h_op <= t_op:
                #print(a, tempStr)
                #print(hash_op)
                ans = a



                if ans in self.solution_list:

                    i = i+1
                else:
                    self.solution_list.append(ans)
                    found = True

                print(self.solution_list, ans)
            else:
                i += 1
                #print(i)


            if time.time() - self.start_time >= 2000:  ## Stop if solution is not found in 2000s ~ 35min
                print(i, a, m, h_op)
                return "NULL", diff, "NULL", i+1

            # if i == 20000001:
            #     return "NULL", diff, "NULL", i-1

        print(hash_op, diff, ans, i+1)
        return ans, diff, hash_op, i+1
