# multithread_task

In this exercise we will be testing your multithreading skills.

Suppose that you want to simulate a fruit farm:

Three farmers are collecting fruits from a single tree to a single dirty fruit basket.

In parallel, three other farmers are getting the fruits from the dirty fruit basket,
cleaning them, and pushing them into the single cleaned fruit basket.

All the farmers are managing the fruit individually

The tree has 50 fruits (and only one farmer at one time can pick fruit from the tree)

Time to collect fruits from the trees into the basket: random(3,6) seconds

Time to clean the fruits into the cleaned fruit basket: random(2,4) seconds

The simulation ends when all the fruits from the tree are collected and cleaned.

The number of fruits in the tree and in the baskets must be logged every second.
