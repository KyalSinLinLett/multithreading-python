import multiprocessing

def calc_square(numbers, result, value):
    
    value.value = 5.667 # update the value from a different process
    
    for idx, num in enumerate(numbers):
        result[idx] = num * num # populate shared array from different process
        
if __name__ == "__main__":
    numbers = [2,3,4]
    
    shared_result_array = multiprocessing.Array('i', 3) # shared array for processes
    
    shared_value = multiprocessing.Value('d', 0.0) # shared value between processes
    
    p1 = multiprocessing.Process(target=calc_square, args=(numbers, shared_result_array, shared_value))
    
    p1.start()
    p1.join()
    
    print(shared_result_array[:])
    print(shared_value.value)