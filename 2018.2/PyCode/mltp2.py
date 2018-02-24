from multiprocessing import Process
import os

def run_proc(name):
    result = 0
    for each in range(100000):
        result = result + 1
    print(result)

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    #p.join()
    print('Child process end.')
