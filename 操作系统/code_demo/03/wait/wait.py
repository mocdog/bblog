import threading
import time

def helper_function(event_obj, timeout, i):
    print("Thread started. for the event to set")
    
    flag = event_obj.wait(timeout)
    if flag:
        print("Event was set to True() earlier, moving ahead with the thread")
    else:
        print("Time out occuered, event internal flag still false,Excuting thread without waiting for event")
        print("Value to be printed=",i)
        
if __name__ == "__main__":
    event_obj = threading.Event()
    
    thread1 = threading.Thread(target=helper_function, args=(event_obj, 3, 27))
    
    thread1.start()
    time.sleep(5)
    
    event_obj.set()
    print("Event is set to True, Now threads can be released.")
    print()