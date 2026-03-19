'''Improving the performance of your program by allowing multiple tasks to run
concurrently'''
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        super().__init__()
        '''Declare threadID and name which are useful in finding and killing a thread.'''
        self.threadID = threadID
        self.name = name
        self.counter = counter

    #Define the execuation flow of a thread
    def run(self):
        print("Starting" + self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting" + self.name)

#A simple work function
def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s: %d" % (threadName, counter))
        counter -= 1

# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)
# Start new Threads
thread1.start()
thread2.start()
print("Exiting Main Thread")

#Modifying shared variables: How to synchronize threads
shared_var = 0
threadLock = threading.Lock()#A lock to a room
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        threadLock.acquire()#One thread gets the lock.
        while self.counter:
            global shared_var
            shared_var += 1
            self.counter -= 1
        threadLock.release()#After using it, return the lock for others.
    
sum_times = 100000
thread1 = MyThread(1, "Thread-1", sum_times)
thread2 = MyThread(2, "Thread-2", sum_times)
thread3 = MyThread(3, "Thread-3", sum_times)
thread1.start()
thread2.start()
thread3.start()
#join(): The main thread will wait until sub-threads are completed.
thread1.join()
thread2.join()
thread3.join()
print(f"Shared value: {shared_var}")
#If we do not use lock or join, shared_var output at each time will be different.