import threading
import time
import random
import os, signal 


 
# Shared Memory variables
CAPACITY = 10
arr = [0 for i in range(5)]
count=0
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0
 
# Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)

# Producer Thread Class
class Producer(threading.Thread):
  
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index, count, arr
    global mutex, empty, full
     
    items_produced = 0
    counter = 0
     
    while items_produced < 20:
      empty.acquire()
      mutex.acquire()
       
      counter =items_produced
      buffer[in_index] = counter
      in_index = (in_index + 1)%CAPACITY
      print("BRIDGES BUILT : ", counter)
      
      mutex.release()
      full.release()
       
      time.sleep(1)
       
      if(count>=5):
          return
      items_produced=input('HOW MANY BLOCKS DO YOU WANT TO LAY?') 
      items_produced=int(items_produced)
      count +=items_produced
    

      #items_produced += 1
 

 
# Consumer Thread Class
class Consumer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index, counter, count, arr
    global mutex, empty, full

    items_consumed = 0
     
    while items_consumed < 10:
      full.acquire()
      mutex.acquire()
      item = random.randint(0,10)
      if(item>count):
        count=0
      
      else:
        count-=item
      
      
      buffer[out_index]=item
      out_index = (out_index + 1)%CAPACITY
      print("\nOH NO! THE DEMON DESTROYED ", item, " BLOCKS!")
      #print("item", item)
      #print("count", count)
      print(" YOU'VE LAID ", count, " BLOCKS SO FAR!")
      if(count>=5):
        #print("BUILD ", 0, "TO WIN")
        print("\nHURRAY!!! YOU'VE DEFEATED THE DEMON, YOU'RE ON THE OTHER SIDE")
      else:
        print("\nDON'T LOSE HOPE, BUILD ", 5-count, "TO WIN")
      arr = [0 for i in range(count)]
      print(arr)
      if(count>=5):
        #print("EXIT")
        return 
        #os.kill(int(0), signal.SIGKILL)
        
      print("---------------------------------------------------------------------------------------------")
       
      mutex.release()
      empty.release()      
       
      time.sleep(2.5)
       
      items_consumed = item
    
 
# Creating Threads
producer = Producer()
consumer = Consumer()
 
# Starting Threads
consumer.start()
producer.start()
 
# Waiting for threads to complete
producer.join()
consumer.join()