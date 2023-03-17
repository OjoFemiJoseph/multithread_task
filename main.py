from multiprocessing import Process, Manager
import time, random
from threading import Lock, Thread, Timer


def every_second():
  global fruit_tree, dirty_fruit, clean_fruit_lst,anchor
  anchor = Timer(1.0, every_second)
  anchor.start()
  print(f" Tree({len(fruit_tree)}) - dirty basket({len(dirty_fruit)}) - Clean Basket({len(clean_fruit_lst)})")

def pop_element_pick(fruit_tree, lock):
        
    if len(fruit_tree) > 0:
        # with lock:
        try:
            if len(fruit_tree) > 0:
                time.sleep(random.randint(3,6))
                fruit = fruit_tree.pop()

                dirty_fruit.append(fruit)
            pop_element_pick(fruit_tree, lock)
        except:
            pass
    else:
        print("List is empty")

def plug_fruit_from_tree(fruit_tree,dirty_fruit,clean_fruit_lst):
    

    lock = Lock()
    
    thread1 = Thread(target=pop_element_pick, args=(fruit_tree, lock))
    thread2 = Thread(target=pop_element_pick, args=(fruit_tree, lock))
    thread3 = Thread(target=pop_element_pick, args=(fruit_tree, lock))
    thread1.start()
    thread2.start()
    thread3.start()

    
    thread1.join()
    thread2.join()
    thread3.join()
    

def clean_fruit(dirty_fruit,clean_fruit_lst,fruit_tree):
    
    def pop_element():
        while len(dirty_fruit) > 0 or len(fruit_tree) > 0:
            # print('i ran',len(dirty_fruit),len(fruit_tree),len(clean_fruit_lst))

            if len(dirty_fruit) > 0:
                time.sleep(random.randint(2,4))
                try:
                    fruit_1 = dirty_fruit.pop()

                    clean_fruit_lst.append(fruit_1)
                except:
                    pass

    thread1 = Thread(target=pop_element)
    thread2 = Thread(target=pop_element)
    thread3 = Thread(target=pop_element)
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == '__main__':
    
    manager= Manager()
    fruit_tree=manager.list(range(1,51))

    length_of_fruit_tree = len(fruit_tree)
    dirty_fruit = manager.list()
    clean_fruit_lst = manager.list()
    every_second()
    p1 = Process(target=plug_fruit_from_tree,args=(fruit_tree,dirty_fruit,clean_fruit_lst))
    p2 = Process(target=clean_fruit, args=(dirty_fruit,clean_fruit_lst,fruit_tree))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    anchor.cancel()
    # print(dirty_fruit)
    print('Number of fruit on tree',length_of_fruit_tree)
    print('Number of fruit in clean basket',len(clean_fruit_lst))