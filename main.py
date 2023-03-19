from multiprocessing import Process, Manager
import time, random
from threading import Lock, Thread

import threading
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)


class FruitProcessor:


    def __init__(self):
        manager= Manager()
        self.fruit_tree=manager.list(range(1,51))

        self.length_of_fruit_tree = len(self.fruit_tree)
        self.dirty_fruit = manager.list()
        self.clean_fruit_lst = manager.list()

    def pop_element_pick(self):
        
        if len(self.fruit_tree) > 0:
            
            try:
                if len(self.fruit_tree) > 0:
                    time.sleep(random.randint(3,6))
                    fruit = self.fruit_tree.pop()

                    self.dirty_fruit.append(fruit)
                
                self.pop_element_pick()
            except:
                pass
        else:
            pass
            # print("List is empty")

    def plug_fruit_from_tree(self):
    

        thread1 = Thread(target=self.pop_element_pick)
        thread2 = Thread(target=self.pop_element_pick)
        thread3 = Thread(target=self.pop_element_pick)
        thread1.start()
        thread2.start()
        thread3.start()

        
        thread1.join()
        thread2.join()
        thread3.join()

    def pop_element(self):
        while len(self.dirty_fruit) > 0 or len(self.fruit_tree) > 0:

            if len(self.dirty_fruit) > 0:
                time.sleep(random.randint(2,4))
                try:
                    fruit_1 = self.dirty_fruit.pop()

                    self.clean_fruit_lst.append(fruit_1)
                except:
                    pass

    def clean_fruit(self):
        
       

        thread1 = Thread(target=self.pop_element)
        thread2 = Thread(target=self.pop_element)
        thread3 = Thread(target=self.pop_element)
        thread1.start()
        thread2.start()
        thread3.start()

        thread1.join()
        thread2.join()
        thread3.join()
    
    def every_second(self):
        
        self.anchor = threading.Timer(1.0, self.every_second)
        self.anchor.start()
        logging.info(f" Tree({len(self.fruit_tree)}) - dirty basket({len(self.dirty_fruit)}) - Clean Basket({len(self.clean_fruit_lst)})")

    def start(self):
        self.every_second()
        p1 = Process(target=self.plug_fruit_from_tree)
        p2 = Process(target=self.clean_fruit)
        p1.start()
        p2.start()

        p1.join()
        p2.join()
        self.anchor.cancel()


if __name__ == '__main__':
    picker = FruitProcessor()
    picker.start()