import time
import threading

def calc_square(arr):
    for n in arr:
        # time.sleep(0.2)
        print(n*n)
        
def calc_cube(arr):
    for n in arr:
        # time.sleep(0.2)
        print(n*n*n)
  
arr = [1,2,3,4,5]      
        
ts = time.time()

# Without multi threading
# calc_square(arr)
# calc_cube(arr)

# With multi threading
thread1 = threading.Thread(target=calc_square, args=(arr,))
thread2 = threading.Thread(target=calc_cube, args=(arr,))

# start threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Time taken:", round(time.time() - ts, 10))
print("done...")