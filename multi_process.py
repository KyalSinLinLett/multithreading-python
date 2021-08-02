import time
import multiprocessing

square_result = []

def calc_square(numbers):
    global square_result
    for n in numbers:
        print('square ' + str(n*n))
        square_result.append(n*n)
    print('within process: ' + str(square_result))
    
if __name__ == "__main__":
    arr = [2,3,8,9]
    
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()
    
    print('result ' + str(square_result))
    print('done...')
    
# a process will have its own memory space(virtual).
# this multi_process.py will be one process
# our calc_square will be one process
# program variables are not shared between two processes
# so when the program is executed, they will run as two separate processes
# so global sqare_result is not shared with calc_square process - it creates a copy of its own
# threads are lightweight processes that run withing a single process
# a process is like its own program under execution - own mem, data
# multiple threads can run within a process by parallelism
