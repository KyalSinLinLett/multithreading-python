from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(10000):
        sum += x*x
        
    return sum

if __name__ == "__main__":
    
    t1 = time.time()
    pool = Pool()
    result = pool.map(f, range(10000))
    pool.close()
    pool.join()
    
    print("Pool took: ", time.time() - t1)
    
    t2 = time.time()
    result = []
    for i in range(10000):
        result.append(f(i))
        
    print("Serial processing took: ", time.time() - t2)