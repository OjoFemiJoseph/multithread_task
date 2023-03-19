from multiprocessing import Process, Manager
import time, random
from threading import Lock, Thread

import threading
import logging

# Set logging format to include timestamp and message, and set logging level to Debug
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


class FruitProcessor:


    def __init__(self):
        """
            Initializes the FruitProcessor object with a fruit tree, a dirty fruit list, and a clean fruit list,
            all managed by a Manager object from the multiprocessing module.
        """

        manager= Manager()
        # Create a list that represents the fruit tree, containing integers 1 to 50, using the Manager object
        self.fruit_tree=manager.list(range(1,51))
        #length of the fruit tree
        self.length_of_fruit_tree = len(self.fruit_tree)
        #a list that represents the dirty fruit basket
        self.dirty_fruit = manager.list()
        #a list that represent the clean fruit basket
        self.clean_fruit_lst = manager.list()

    def pop_element_pick(self):
        """
            Picks a fruit from the fruit tree and adds it to the dirty fruit basket.
            This function is recursively called until there are no more fruits in the fruit tree.
        """
        
        # Check if there are still fruits on the fruit tree
        if len(self.fruit_tree) > 0:
            
            try:
                # Wait for a for few seconds before picking a fruit from the tree
                time.sleep(random.randint(3,6))
                # Remove a fruit from the fruit tree
                fruit = self.fruit_tree.pop()
                # Add the fruit to the dirty fruit basket
                self.dirty_fruit.append(fruit)
                
                self.pop_element_pick()
            except:
                pass
        else:
            pass


    def plug_fruit_from_tree(self):
    
        """
            Start three threads to represent 3 farmers to pick fruits from the fruit tree and add them to the dirty fruit basket.
        """
        thread1 = Thread(target=self.pop_element_pick)
        thread2 = Thread(target=self.pop_element_pick)
        thread3 = Thread(target=self.pop_element_pick)
        # Start the first thread
        thread1.start()
        # Start the second thread
        thread2.start()
        # Start the third thread
        thread3.start()

        # Wait for the first thread to finish
        thread1.join()
        # Wait for the second thread to finish
        thread2.join()
        # Wait for the third thread to finish
        thread3.join()

    def pop_element(self):
        """
        This method checks the dirty fruit basket until the fruit tree and the basket are both empty    
        """
        while len(self.dirty_fruit) > 0 or len(self.fruit_tree) > 0:

            time.sleep(random.randint(2,4))
            try:
                # Remove a fruit from the dirty basket
                fruit_1 = self.dirty_fruit.pop()
                # Add the fruit to the clean fruit basket
                self.clean_fruit_lst.append(fruit_1)
            except:
                pass

    def clean_fruit(self):
        """
            Start three threads to represent 3 cleaners to pick fruits from the dirty fruit basket and add them to the clean fruit basket.
        """

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
        """
            log the content of the fruit tree , dirty basket and clean basket every second
        """
        self.anchor = threading.Timer(1.0, self.every_second)
        self.anchor.start()
        logging.info(f" Tree({len(self.fruit_tree)}) - dirty basket({len(self.dirty_fruit)}) - Clean Basket({len(self.clean_fruit_lst)})")

    def start(self):
        """
            This method starts the fruit processing by creating two processes, one for plucking fruits from the tree 
            and another for cleaning the fruits. It also starts a timer to print the status of the processing every second.
        """
        self.every_second()
        # creates a process to pluck fruits from the tree
        p1 = Process(target=self.plug_fruit_from_tree)
        # creates a process to clean fruits inside the dirty basket
        p2 = Process(target=self.clean_fruit)
        #starts the first process of plucking the fruit from tree
        p1.start()
        #starts the process of cleaning the fruit
        p2.start()

        p1.join()
        p2.join()
        #stop the method that prints the contents every second
        self.anchor.cancel()


if __name__ == '__main__':
    picker = FruitProcessor()
    picker.start()