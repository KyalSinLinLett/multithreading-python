import multiprocessing
import time

def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)
        
if __name__ == "__main__":
    
    numbers = [1,2,3,4]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square, args=(numbers, q))
    p1.start()
    time.sleep(1.0)
    p1.join

    while not q.empty():
        print(q.get())