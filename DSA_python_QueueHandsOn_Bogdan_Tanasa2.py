#!/usr/bin/env python
# coding: utf-8

# ### **Homework Problem 1: Queue Operations**
# 
# Write a Python class that implements a Queue data structure using a Python list with the following methods:
# 
# **enqueue(item):** Add an item to the rear of the queue.
# 
# **dequeue():** Remove and return the front item from the queue.
# 
# **peek():** Return the front item without removing it.
# 
# **is_empty():** Check if the queue is empty.
# 
# **size():** Return the number of elements in the queue.

# In[17]:


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("The list is empty.")
        else:
            return self.items.pop(0)

    def peek(self):
         if len(self.items) == 0:
            print("The list is empty.")
         else:
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0         # Check if the queue is empty

    def size(self):
        return len(self.items)              # Return the number of elements in the queue

# Test the Queue class
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue)
print(queue.dequeue())    # Output: 10
print(queue.peek())       # Output: 20
print(queue.is_empty())   # Output: False
print(queue.size())       # Output: 2


# ### **Homework Problem 2: Hot Potato Game**
# 
# Write a Python function that simulates the "Hot Potato" game using a queue. The function should take a list of names and a positive integer as input, representing the number of passes. The function should return the name of the last person remaining after repeatedly passing the potato.
# 
# **Variarions**: Think of how the solution can be modified so that a different player has a chance of winning if played multiple times.

# In[18]:


def hot_potato(names, passes):

    queue = names   
    number_passes = passes 
    
    # Use a while expression to continue until only one person is left
    while len(queue) > 1:
        
        for number_pass in range(number_passes):  # Passing the potato 'passes" times
                                                  # As the potato is passed, the first person is moved to the end of the list
            first_person = queue.pop(0)  
            queue.append(first_person)     
            
        queue.pop(0)                              # This person did hold the potato
    return queue[0]                               # This is the last person remaining in the game  
 
names_list = ["Alice", "Bob", "Charlie", "David", "Eva"]
passes_count = 3

print("The last remaining person's name :")
print(hot_potato(names_list, passes_count))  


# ### **Homework Problem 3: Bank Counter Simulation**
# 
# Write a Python function that simulates a bank counter using a queue to manage customers. The function should take a list of customers' arrival times and their transaction times as input. The function should return the total waiting time for all customers.
# 
# Note: The goal of this problem is to calculate the total waiting time for all customers using a queue to manage their order of service. The waiting time for each customer is the difference between the time they start their transaction and their arrival time.
# 
# Here is an example to help you understand the calculation:
# 
# Example:
# 
# Arrival Times: [0, 2, 5, 10]
# Transaction Times: [3, 6, 4, 2]
# Calculation Steps:
# 
# Customer 1 arrives at time 0 and takes 3 units of time. They start immediately, so their waiting time is 0.
# 
# Customer 2 arrives at time 2 and takes 6 units of time. They start at time 3 (after Customer 1 finishes), so their waiting time is 1 (3 - 2).
# 
# Customer 3 arrives at time 5 and takes 4 units of time. They start at time 9 (after Customer 2 finishes), so their waiting time is 4 (9 - 5).
# 
# Customer 4 arrives at time 10 and takes 2 units of time. They start at time 13 (after Customer 3 finishes), so their waiting time is 3 (13 - 10).
# 
# The total waiting time is the sum of all individual waiting times: 0 + 1 + 4 + 3 = 8.

# In[19]:


def bank_counter(arrival_times, transaction_times):
    
    total_waiting_time = 0
    monitoring_time = 0

    # Monitoring each customer's waiting time
    
    for i in range(len(arrival_times)):
    
        arrival_time = arrival_times[i]       
        transaction_time = transaction_times[i]  

        # If the customer arrives after the current time, we update monitoring_time to the time of its arrival ; 
        # there is no waiting time 
        
        if monitoring_time < arrival_time:
             monitoring_time = arrival_time       # Update the monitoring_time to the customer's arrival time
        
        # Calculate waiting time for this customer
        waiting_time = monitoring_time - arrival_time
        
        # Add this customer's waiting time to the total
        total_waiting_time += waiting_time
        
        # Update current time to account for this customer's transaction
        monitoring_time += transaction_time

    return total_waiting_time

# Test the bank_counter function
arrival_times_list = [0, 2, 5, 10]
transaction_times_list = [3, 6, 4, 2]

print("Total waiting time :")
print(bank_counter(arrival_times_list, transaction_times_list))  


# In[ ]:





# ### **Bonus**
# 
# Implement **queue** using **linked list** examples provided in the lecture notes.
# 
# Learn how stack can be implemented using linkedlist by going through this visualization website: https://www.cs.usfca.edu/~galles/visualization/QueueLL.html
