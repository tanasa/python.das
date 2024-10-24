#!/usr/bin/env python
# coding: utf-8

# **Slide 1: Overview of Python Collections Module**
# 
# collections module provides alternative container datatypes to built-in containers.
# 
# Special data structures: namedtuple, deque, Counter, defaultdict, and OrderedDict.
# 

# In[1]:


# Adaptation and extension of an material provided by Beneet Sharma.


# **Practical Usage:** The collections module is widely used in various applications for its efficient and specialized data structures, making it easier to solve specific problems that arise when working with collections of data.

# **Slide 2: namedtuple**
# 
# namedtuple is a subclass of tuples that have named fields, making code more readable and self-documenting. It can be used to create simple classes for holding data.

# In[2]:


# Example Practical Usage of namedtuple
from collections import namedtuple

# Define a namedtuple for representing a book
Book = namedtuple('Book', ['title', 'author', 'genre'])

# Create an instance of Book
book1 = Book('Python Crash Course', 'Eric Matthes', 'Programming')

# Access the fields using dot notation
print("Title:", book1.title)    # Output: Title: Python Crash Course
print("Author:", book1.author)  # Output: Author: Eric Matthes
print("Genre:", book1.genre)    # Output: Genre: Programming


# In[3]:


# Namedtuple to represent a 3D point in space:
from collections import namedtuple

# Define a namedtuple for a 3D point
Point3D = namedtuple('Point3D', ['x', 'y', 'z'])

# Create an instance of Point3D
point1 = Point3D(10, 20, 30)

# Access the fields using dot notation
print("X-coordinate:", point1.x)  # Output: X-coordinate: 10
print("Y-coordinate:", point1.y)  # Output: Y-coordinate: 20
print("Z-coordinate:", point1.z)  # Output: Z-coordinate: 30

# Calculate the distance from the origin (0, 0, 0)
distance = (point1.x**2 + point1.y**2 + point1.z**2)**0.5
print("Distance from origin:", distance)  # Output: Distance from origin: 37.416573867739416


# In[4]:


# A comparison between Regular Tuples and Named Tuples

# Regular tuple access
person = ('Alice', 30, 'Engineer')
print(person[0])  

# namedtuple access : much clearer code

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'profession'])
person = Person(name='Alice', age=30, profession='Engineer')
print(person.name) 


# **Practical Usage:** Namedtuples are commonly used for representing data records, such as database rows, API responses, or configuration settings, as they provide a convenient way to access fields using descriptive names.
# 
# 

# ### **Slide 3: deque**
# Data structure for efficient append and pop operations from both ends.
# 
# Useful for implementing queues and stacks.
# 
# **Practical Usage:** Deques are commonly used in scenarios where efficient insertions and deletions are required from both ends of a collection.
# One example is managing a playlist where you need to add and remove songs from the front or back.

# In[5]:


# Example Practical Usage of deque
from collections import deque

# Create a deque for a playlist
playlist = deque()

# Add songs to the playlist
playlist.appendleft("Song 1")   # Adds "Song 1" to the front (left) of the deque
playlist.append("Song 2")       # Adds "Song 2" to the back (right) of the deque
playlist.appendleft("Song 3")   # Adds "Song 3" to the front again, pushing "Song 1" and "Song 2" further back.

print("Showing the content of the playlist after adding the songs :")
print(playlist)

# Play the next song and remove it from the playlist
print("Now playing :", playlist.popleft())  # Output: Now playing: Song 3
# Removes and returns the song at the front of the deque (left side). 
# In this case, "Song 3" is the first song, so it is played and removed from the playlist.

# Remaining playlist
print("The songs in the playlist :")
print(playlist)  # Output: deque(['Song 1', 'Song 2'])


# In[6]:


# The deque (double-ended queue) allows fast appends and pops from both ends, 
# which makes it ideal for use cases like queues or stacks. 

# The methods in dequeue() are the following :
# Adding Elements: append(), appendleft(), extend(), extendleft(), insert()
# Removing Elements: pop(), popleft(), remove(), clear()
# Reordering: rotate(), reverse()
# Utility Methods: count(), maxlen


# In[7]:


from collections import deque

# Create a deque with a maximum length of 5
playlist = deque(maxlen=5)

# 1. append(x) - Adds an element to the end (right side)
playlist.append("Song A")
playlist.append("Song B")
print("After append (Song A, Song B):", playlist)

# 2. appendleft(x) - Adds an element to the beginning (left side)
playlist.appendleft("Song C")
print("After appendleft (Song C):", playlist)

# 3. extend(iterable) - Adds multiple elements to the right side
playlist.extend(["Song D", "Song E"])
print("After extend (Song D, Song E):", playlist)

# 4. extendleft(iterable) - Adds multiple elements to the left, in reverse order
playlist.extendleft(["Song F", "Song G"])  # Adds G, F
print("After extendleft (Song F, Song G):", playlist)  # Song G gets added first, then Song F

# 5. pop() - Removes and returns the last element (right side)
print("Popped element:", playlist.pop())
print("After pop:", playlist)

# 6. popleft() - Removes and returns the first element (left side)
print("Popped left element:", playlist.popleft())
print("After popleft:", playlist)

# 7. remove(value) - Removes the first occurrence of a value
playlist.append("Song H")
print("Before remove (Song H added):", playlist)
playlist.remove("Song H")
print("After remove (Song H):", playlist)

# 8. rotate(n) - Rotates the deque n steps to the right (positive) or left (negative)
playlist.rotate(1)  # Rotate one step to the right
print("After rotate right (1 step):", playlist)
playlist.rotate(-2)  # Rotate two steps to the left
print("After rotate left (2 steps):", playlist)

# 9. reverse() - Reverses the elements in the deque
playlist.reverse()
print("After reverse:", playlist)

# 10. clear() - Removes all elements from the deque
# playlist.clear()
# print("After clear:", playlist)

# 11. count(value) - Counts occurrences of a value
playlist.extend(["Song A", "Song B", "Song A", "Song C", "Song A"])
print("Playlist with duplicates:", playlist)
count_A = playlist.count("Song A")
print(f"Count of 'Song A': {count_A}")

# 12. insert(i, x) - Inserts an element at a specific position
# playlist.insert(1, "Song X")  # Insert "Song X" at index 1
# print("After insert (Song X at index 1):", playlist)

# 13. maxlen - Maximum length of the deque
print("Maximum length of the deque:", playlist.maxlen)


# In[8]:


# You can iterate over a deque in Python using a for loop just like you would with a list. 
# The deque allows you to traverse through its elements in the order they are stored. 

from collections import deque

# Create a deque with some elements
playlist = deque(["Song A", "Song B", "Song C", "Song D"])

# Use a for loop to iterate over the deque
print("Iterating over the playlist:")
for song in playlist:
    print(song)

# Use a for loop to iterate and modify elements
print("Updating songs in the playlist:")
for i, song in enumerate(playlist):
    playlist[i] = song + " (Updated)"     # Example: Append " (Updated)" to each song

# Display updated playlist
print("Updated playlist:")
for song in playlist:
    print(song)
    
# We can access and modify elements in a deque using indexing, 
# similar to how you would with lists.


# In[9]:


# A deque (double-ended queue) in Python can serve as a list, queue, and stack due to its versatile functionality. 

# 1. As a List
# A deque can be used similarly to a list, allowing for indexing, slicing, and iteration. 
# However, it is more optimized for adding and removing items from both ends rather than random access.

from collections import deque

# Using deque as a list
print("Using dequeue as a list :")
my_list = deque(["A", "B", "C"])
print(my_list)
print("the 1st element : ")
print(my_list[1])  # Accessing element at index 1
print("the 1st element after a change :")
my_list[1] = "D"   # Modifying element at index 1
print(my_list)     # Output: deque(['A', 'D', 'C'])


# In[10]:


# A dequeue as a Queue

# A deque is ideal for implementing a queue, allowing for efficient FIFO (First In, First Out) operations. 
# You can use append() to add items to the end and popleft() to remove items from the front.


from collections import deque

# Using deque as a queue
queue = deque()

queue.append("First")
queue.append("Second")
queue.append("Third")

print(queue.popleft())  # Output: First
print(queue)            # Output: deque(['Second', 'Third'])


# In[11]:


# A deque can also be used as a Stack, enabling efficient LIFO (Last In, First Out) operations. 
# You can use append() to push items onto the stack and pop() to remove them from the top.

from collections import deque

# Using deque as a stack
stack = deque()

stack.append("First")
stack.append("Second")
stack.append("Third")

print(stack.pop())  # Output: Third
print(stack)        # Output: deque(['First', 'Second'])


# In[12]:


# There is an alternative library and class Queue from the queue module

# The queue.Queue class provides thread-safe FIFO semantics, making it suitable for multithreading.
# Operations: Use put() to add items and get() to remove items.


import queue

# Using queue.Queue
q = queue.Queue()
q.put("First")
q.put("Second")
print(q.get())  # Output: First

# Print and store the contents of the queue
items = []

while not q.empty():
    item = q.get()      # Remove item from the queue
    items.append(item)  # Store it for printing

# Print the items
print("Contents of the queue:")
for item in items:
    print(item)

# Rebuild the queue with the original items
for item in items:
    q.put(item)


# In[13]:


# Stack from the queue module

#  Usage: You can use queue.LifoQueue for stack behavior (LIFO).
#  Operations: Use put() to add items and get() to remove items.

import queue

# Create a LifoQueue (stack) and add some elements
stack = queue.LifoQueue()
stack.put("First")
stack.put("Second")
stack.put("Third")

# Print the contents of the stack without altering its original state
print("Contents of the stack:")

# Use a temporary list to hold the items
temp_items = []

# Extract and print items while storing them in the temporary list
while not stack.empty():
    item = stack.get()         # Remove item from the stack
    print(item)                # Print the item
    temp_items.append(item)    # Store the item in the temporary list

# Rebuild the stack with the original items
for item in reversed(temp_items):
    stack.put(item)  # Put the items back in the original order


# ### **Slide 4: Counter**
# Subclass of dictionary used to count occurrences of elements.
# 
# Works with collections like list, tuple, or string.
# 
# **Practical Usage:** Counters are valuable for counting occurrences of elements in collections. They are widely used in text analysis, data preprocessing, and frequency analysis tasks.

# In[14]:


# Example Practical Usage of Counter
from collections import Counter

# Count the frequency of words in a text
text = "Python is a popular programming language for data analysis and machine learning. Python can be used for OOP and game programming as well."
word_counter = Counter(text.split())

# Most common words
print(word_counter.most_common(9))  
# [('Python', 1), ('is', 1), ('a', 1), ('popular', 1), ('programming', 1), ('language', 1)]

print("the type of the data structure :")
print(type(word_counter))

# Print all words and their frequencies
print("Word frequencies:")
for word, count in word_counter.items():
    print(f"{word}: {count}")
    
# To get the frequency of the first element (word) from the Counter object in your code, 
# you can access the first element directly after splitting the text. 

# Get the first element
first_word = text.split()[0]  # This will give you the first word, which is 'Python'

# Get the frequency of the first element
first_word_frequency = word_counter[first_word]

# Print the frequency of the first element
print(f"The frequency of '{first_word}' is: {first_word_frequency}")


# ### **Slide 5: defaultdict**
# Subclass of dictionary with a default value for missing keys.
# 
# 
# Prevents KeyError for missing keys.
# 
# **Practical Usage:** Defaultdicts are useful when dealing with nested data structures, especially when aggregating data or building complex data models.

# In[15]:


# Example Practical Usage of defaultdict
from collections import defaultdict

#  A defaultdict is a type of dictionary that provides a default value for nonexistent keys, 
# which helps avoid KeyError.

# Create a defaultdict to group students by their favorite subjects
# A list of tuples called students is created. 
# Each tuple contains a student's name and their favorite subject.

students = [('Alice', 'Math'), ('Bob', 'History'), ('Alice', 'History'), ('Bob', 'Math')]

subject_groups = defaultdict(list)
for student, subject in students:
    subject_groups[student].append(subject)
    
# defaultdict(list): Automatically creates an empty list for any new key that doesn't exist yet.
# When you do subject_groups[student].append(subject), 
# if student is not yet in subject_groups, 
# it automatically creates an entry with an empty list. 
# You can then append to that list without needing to check if the key exists.

# Group students by their favorite subjects
print(dict(subject_groups))
# Output: {'Alice': ['Math', 'History'], 'Bob': ['History', 'Math']}

# Iteration: The loop iterates over each tuple in the students list. 
# For each tuple, it unpacks the values into the variables student and subject.

# First Iteration: student = 'Alice', subject = 'Math'
# Second Iteration: student = 'Bob', subject = 'History'
# Third Iteration: student = 'Alice', subject = 'History'
# Fourth Iteration: student = 'Bob', subject = 'Math'

# Appending Subjects: Inside the loop, it performs the following actions:
# Accessing the Key: subject_groups[student] accesses the list corresponding to the student key in the subject_groups dictionary.
# Appending the Subject: The append(subject) method adds the current subject to the list for that student.

# After the loop completes, the subject_groups dictionary will look like this:
# {
#    'Alice': ['Math', 'History'],
#    'Bob': ['History', 'Math']
# }


# ### **Slide 6: OrderedDict**
# 
# Dictionary subclass that maintains the order of insertion of keys.
# 
# Useful for preserving the order of elements.
# 
# **Practical Usage:** OrderedDicts are valuable when you need to process elements in the order they were added.
# One use case is building URL query parameters, where the order matters.
# 

# 

# In[16]:


# Example Practical Usage of OrderedDict
from collections import OrderedDict

# Create an ordered dictionary for URL query parameters
query_params = OrderedDict()
query_params['page'] = 1
query_params['sort'] = 'name'
query_params['filter'] = 'category'

# Generate URL with query parameters
url = '/products?' + '&'.join(f"{key}={value}" for key, value in query_params.items())
print(url)          # Output: /products?page=1&sort=name&filter=category


# In[17]:


# We will create an OrderedDict to store and display a list of products along with their prices, 
# ensuring that the order in which products are added is preserved.

from collections import OrderedDict

# Create an OrderedDict to store products and their prices
product_prices = OrderedDict()

# Adding products
product_prices['Apple'] = 0.50
product_prices['Banana'] = 0.30
product_prices['Cherry'] = 0.75
product_prices['Date'] = 1.00

# Display the product prices in the order they were added
print("Product Prices:")
for product, price in product_prices.items():
    print(f"{product}: ${price:.2f}")

# Output:
# Product Prices:
# Apple: $0.50
# Banana: $0.30
# Cherry: $0.75
# Date: $1.00


# In[18]:


# Counting Frequency of Words While Maintaining Order

# In this example, we will use OrderedDict to count the frequency of words in a sentence 
# while preserving the order of their first appearance.

from collections import OrderedDict

# Sample sentence
sentence = "apple banana apple orange banana apple"

# Create an OrderedDict to count word frequencies
word_count = OrderedDict()

# Split the sentence into words and count frequencies
for word in sentence.split():
    if word not in word_count:     # If the word is not in the dictionary, initialize its count
        word_count[word] = 0
    word_count[word] += 1          # Increment the count for the word

# Display word frequencies in order of first appearance
print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# Output:
# Word Frequencies:
# apple: 3
# banana: 2
# orange: 1


# **Slide 7: ChainMap**
# 
# Groups multiple dictionaries as a single unit.
# 
# Enables easy searching in multiple dictionaries.
# 
# **Practical Usage:** ChainMaps are useful for managing configuration settings in a hierarchical manner, allowing easy access and overriding of values from multiple sources.

# In[19]:


# Example Practical Usage of ChainMap
from collections import ChainMap

# Define two dictionaries for configuration settings
default_config = {'timeout': 30, 'max_attempts': 3}
user_config = {'timeout': 60, 'log_level': 'INFO'}

print("1st dictionary : default config :")
print(default_config)
print("2nd dictionary : user_config :")
print(user_config)

# Create a ChainMap with the dictionaries ;
# This line creates a ChainMap object called combined_config, combining user_config and default_config. 
# In a ChainMap, keys in the first dictionary (in this case, user_config) take precedence over those 
# in subsequent dictionaries (like default_config).
combined_config = ChainMap(user_config, default_config)

print("the ChainMap : combine_config :")
print(combined_config)

# Access values using keys from both dictionaries
print(combined_config['timeout'])       # Output: 60 (value from user_config, as it takes precedence)
print(combined_config['max_attempts'])  # Output: 3 (value from default_config)
print(combined_config['log_level'])     # Output: INFO (value from user_config)


# In[20]:


# Access the first and second dictionaries
user_config_accessed = combined_config.maps[0]
default_config_accessed = combined_config.maps[1]

# Print the accessed dictionaries
print("Accessed first dictionary (user_config):", user_config_accessed)
print("Accessed second dictionary (default_config):", default_config_accessed)


# ### **Slide 8: namedtuple - Advanced Usage**
# 
# Supports default values for fields.
# 
# Can replace or modify fields in an instance.
# 
# **Practical Usage:** Namedtuples with default values are convenient when working with data records that have optional fields or settings. They provide a clean way to handle default values when a particular field is missing.

# In[21]:


# Example Practical Usage of namedtuple with default values
from collections import namedtuple

# Define a namedtuple for representing a Circle with default radius=0
Circle = namedtuple('Circle', ['x', 'y', 'radius'], defaults=[0])

# Create an instance of Circle with only x and y coordinates
circle1 = Circle(3, 4)

# Create another instance with additional radius
circle2 = circle1._replace(radius=5)

# Access fields
print(circle1)  # Output: Circle(x=3, y=4, radius=0)
print(circle2)  # Output: Circle(x=3, y=4, radius=5)


# In[22]:


# Reasons for _replace() :

# Namedtuples in Python are IMMUTABLE, meaning that once they are created, 
# their fields cannot be changed. 
# This is a key feature that provides safety against unintended modifications.
# Because of immutability, if you need to change any attribute of a namedtuple, 
# you cannot directly modify the existing instance. 
# Instead, you must create a new instance with the desired changes.

# Creating a New Instance:
# The _replace() method creates a new instance of the namedtuple with specified fields replaced by new values. 
# In this case, it creates a new Circle instance with the same x and y values as circle1, 
# but updates the radius to 5.

# Convenience:

# Using _replace() is a convenient way to create a modified version of an existing instance without having 
# to provide all the field values again. You only need to specify the fields that you want to change.
# It maintains the original instance (circle1), which can still be used elsewhere without being altered.


# **Slide 9: deque - Rotate and Extend**
# 
# Supports rotation to the right or left.
# 
# Can extend with elements from another iterable.
# 
# **Practical Usage:** Deques with rotation are valuable when implementing algorithms that involve cyclic shifts or circular buffers.
# Extending deques is useful for combining collections or efficiently appending multiple elements.

# In[23]:


# Example Practical Usage of deque with rotation and extension
from collections import deque

# Create a deque for a circular buffer
circular_buffer = deque(maxlen=5)

# Add elements to the buffer
circular_buffer.append(1)
circular_buffer.append(2)
circular_buffer.append(3)
circular_buffer.append(4)
circular_buffer.append(5)

# Now the buffer is full (maxlen=5)
print(circular_buffer)            # Output: deque([1, 2, 3, 4, 5], maxlen=5)

# Add another element, which causes the oldest element (1) to be removed
circular_buffer.append(6)
print(circular_buffer)             # Output: deque([2, 3, 4, 5, 6], maxlen=5)

# Rotate the deque to the right by 2 positions
circular_buffer.rotate(2)
print(circular_buffer)             # Output: deque([5, 6, 2, 3, 4], maxlen=5)

# Extend the deque with another iterable (list)
circular_buffer.extend([7, 8, 9])
print(circular_buffer)             # Output: deque([3, 4, 7, 8, 9], maxlen=5).  Basically

# it is the same as appending one element, multiple times.


# **Slide 10: Counter - Arithmetic Operations**
# 
# Supports addition, subtraction, intersection, and union.
# 
# Convenient for working with countable data.
# 
# **Practical Usage:** Counters are widely used in data analysis, text processing, and machine learning tasks for merging and analyzing frequency data from different sources.

# In[24]:


# Example Practical Usage of Counter with arithmetic operations
from collections import Counter

# Define two Counters for word frequency
text1 = "Python is a popular programming language."
text2 = "Python is used for data analysis and machine learning."

word_counter1 = Counter(text1.split())
print(word_counter1)
word_counter2 = Counter(text2.split())
print(word_counter2)

# Combine word frequencies from both texts
combined_counter = word_counter1 + word_counter2
print(combined_counter)

# Output: Counter({'Python': 2, 'is': 2, 'a': 1, 'popular': 1, 'programming': 1,
#                 'language.': 1, 'used': 1, 'for': 1, 'data': 1, 'analysis': 1,
#                 'and': 1, 'machine': 1, 'learning.': 1})


# ### **Slide 11: defaultdict - Advanced Usage**
# 
# Can use complex data types as the default_factory.
# 
# Allows nested defaultdicts for more complex structures.
# 
# **Practical Usage:** Nested defaultdicts are helpful when constructing complex data structures, such as multi-level dictionaries, without manually checking and creating missing keys.
# 
# **Explanation **
# 
# **Nested defaultdict Initialization:****
# 
# You want student_scores to be a defaultdict where each value is another defaultdict that returns 0 for any missing key. This requires the default_factory of the outer defaultdict to be another defaultdict with an integer default.
# 
# **Using lambda:**
# 
# The lambda function lambda: defaultdict(int) serves as a factory for creating new defaultdict(int) instances. When a key is accessed that does not exist, the lambda function is called to provide a new defaultdict(int) as the default value.

# In[25]:


# Example Practical Usage of defaultdict with complex default_factory
from collections import defaultdict

# Define a nested defaultdict to store student scores
student_scores = defaultdict(lambda: defaultdict(int))

# Add scores for students and their subjects
student_scores['Alice']['Math'] = 95
student_scores['Alice']['History'] = 87
student_scores['Bob']['Math'] = 78
student_scores['Bob']['History'] = 90

# Access the keys-values pairs :
print(student_scores['Alice'])  
print(student_scores['Bob'])  

# Access the scores
print(student_scores['Alice']['Math'])  # Output: 95
print(student_scores['Bob']['History'])  # Output: 90


# In[26]:


# A DEFAULT FACTORY :

# a default factory is a callable (like a function or a lambda) that provides a default value for a defaultdict 
# when a key that does not exist is accessed.

# Complex Default Factory

# A complex default factory refers to a situation where the default factory itself creates a data structure 
# that can have its own default behavior. 
# This is particularly useful for creating nested dictionaries, lists, or other collections without needing 
# to initialize them explicitly each time.

my_dict = defaultdict(lambda: defaultdict(int))

# Accessing a key that does not exist
print("Accessing a non-existing key 'apple':", my_dict['apple'])  # Output: 0

# Now, let's add some values
my_dict['banana'] = 2

# Accessing an existing key
print("Accessing an existing key 'banana':", my_dict['banana'])         # Output: 2

# Accessing another non-existing key 'grape'
print("Accessing another non-existing key 'grape':", my_dict['grape'])  # Output: 0

# Current state of the defaultdict
print("Current state of the defaultdict:", dict(my_dict))              # Output: {'apple': 0, 'banana': 2, 'grape': 0}


# Here’s a breakdown of how this works:

# Outer defaultdict: This defaultdict uses a lambda function as its default factory. 
# When you try to access a key that doesn’t exist (like 'Alice' or 'Bob'), it will automatically create 
# a new defaultdict as the value for that key.

# Inner defaultdict: The inner defaultdict is initialized with int as its default factory, 
# which means that any key accessed within this nested structure that doesn’t exist will have 
# a default value of 0 (since int() returns 0).


# ### **Slide 12: OrderedDict - Pop and Move to End**
# 
# Supports popping the first or last item.
# 
# Can move an item to the end (last) position.
# 
# **Practical Usage: **OrderedDicts can be useful for building LRU (Least Recently Used) caches where you need to manage the order of items based on their access frequency.

# In[27]:


# Example Practical Usage of OrderedDict with pop and move_to_end
from collections import OrderedDict

# Create an OrderedDict for an LRU cache with maximum capacity of 3
cache = OrderedDict()

# Add items to the cache
cache['item1'] = 100
cache['item2'] = 200
cache['item3'] = 300

# Access item2, which moves it to the end (most recently used)
print(cache['item2'])  # Output: 200

# Accessing item1 will move it to the end as it becomes the most recently used
print(cache['item1'])  # Output: 100

# Adding a new item will remove the oldest item (item3) due to the LRU cache's capacity
cache['item4'] = 400
print(cache)  # OrderedDict([('item1', 100), ('item2', 200), ('item3', 300), ('item4', 400)])


# In[28]:


# Creating an OrderedDict from a List of Tuples, which can be useful for initializing it with existing data.

data = [('apple', 1), ('banana', 2), ('orange', 3)]
ordered_dict = OrderedDict(data)

print(ordered_dict)  


# In[29]:


from collections import OrderedDict

# Creating an OrderedDict
ordered_dict = OrderedDict()

# Adding items
ordered_dict['apple'] = 1
ordered_dict['banana'] = 2
ordered_dict['orange'] = 3

# Display the OrderedDict
print(ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])

# Order is maintained
for key, value in ordered_dict.items():
    print(key, value)
# Output:
# apple 1
# banana 2
# orange 3


# In[30]:


# Adding another fruit
ordered_dict['grape'] = 12

# Display the OrderedDict
print(ordered_dict)  # Output: OrderedDict([('apple', 10), ('banana', 5), ('orange', 8), ('grape', 12)])

# Move 'apple' to the end
ordered_dict.move_to_end('apple')

# Display the OrderedDict
print(ordered_dict)  

# Deleting an Element
# You can delete elements just like a regular dictionary, and the order will still be maintained.

# Remove 'banana'
del ordered_dict['orange']

# Display the OrderedDict
print(ordered_dict)

# Get keys, values, and items
print(ordered_dict.keys())   
print(ordered_dict.values()) 
print(ordered_dict.items())  


# In[ ]:




