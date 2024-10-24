#!/usr/bin/env python
# coding: utf-8

# ## **HandsOn**
# ### **Homework Problem 1: Parentheses Checker**
# Write a Python function that takes a string as input and checks if the parentheses in the expression are balanced or not. Use the StackUsingDeque class to implement the stack.

# In[42]:


from collections import deque

class StackUsingDeque:           # we import the code from the lecture on Stacks
                                 # deque is a class in the collections module of Python 
                                 # that provides a double-ended queue, that allows us 
                                 # to efficiently append and remove elements from both ends 
                                 # the left and right sides), 
                        
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def is_matching_pair(left, right):
    
    """Check if the left and right brackets match."""
    if (left == '(' and right == ')') or        (left == '{' and right == '}') or        (left == '[' and right == ']'):
        return True
    return False

# The implementation will involve using a stack to keep track of opening brackets 
# and checking for matching closing brackets as we traverse the string.

def is_balanced(expression):
    """Check if the brackets in the expression are balanced."""
    
    a_stack = StackUsingDeque()  
    
    for a_character in expression:

        if a_character in '({[':                    
            a_stack.push(a_character)                              # Pushing the brackets onto the stack
            
        elif a_character in ')}]':
            if a_stack.is_empty():  
                return False
            
            if not is_matching_pair(a_stack.pop(), a_character):  # Check for a matching pair
                return False
 
    return a_stack.is_empty()  # Return True if all brackets are balanced

# We have chosen to work with a stack of '({[' or ')}]'
# The statement return a_stack.is_empty() is crucial in the is_balanced function because 
# it checks whether all opening brackets have been properly matched and closed. 


# Tests
expr1 = "{89/{7+[x*(5+6)]}+40}"
expr2 = "{[()]}({[data1]})[more(data2)]"
expr3 = "function(arg1, {key: [value1, value2]})"
expr4 = "{[()]({[data1]}[more(data2)]"
expr5 = "function(arg1, {key: [value1, value2]))"
print(is_balanced(expr1))  # Output: True
print(is_balanced(expr2))  # Output: True
print(is_balanced(expr3))  # Output: True
print(is_balanced(expr4))  # Output: False
print(is_balanced(expr5))  # Output: False


# In[ ]:





# ### **Homework Problem 2: Decimal to Binary Conversion**
# 
# Write a Python function that takes an integer as input and converts it into its binary representation.
# Use the StackUsingList class to implement the stack.

# In[43]:


class StackUsingList:
    def __init__(self):
        self.items = [] # using list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def decimal_to_binary(number):
    
    # We use a stack to keep the binary digits 
    a_stack = StackUsingList()

    while number > 0:
        the_remainder = number % 2  
        a_stack.push(the_remainder)  
        number = number // 2

    # Transfer the binary digits to a list
    binary_digits = []
    while not a_stack.is_empty():
        binary_digits.append(a_stack.pop())  # Pop from the stack and append to the list

    # Join the binary digits to form the final binary string
    binary_digits_string = ''.join(str(digit) for digit in binary_digits)
    
    return binary_digits_string

# Test
num1 = 10
num2 = 42
print(decimal_to_binary(num1))  # Output: 1010
print(decimal_to_binary(num2))  # Output: 101010


# # **Homework Problem 3: Function Call Trace**
# 
# Write a Python function that takes a positive integer as input and prints the trace of the function call stack for the factorial function.
# Use the StackUsingList class to implement the stack.

# In[44]:


class StackUsingList:
    def __init__(self):
        self.items = []  # Using list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def factorial(n, stack):

    # n (int): The number to compute the factorial of.
    # stack (StackUsingList): The stack to record function calls.
    
    # Push the current function call onto the stack
    stack.push(f"factorial({n})")
    
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1, stack)
    
    # Optionally, you can pop here if you want the stack to reflect the current call stack
    # stack.pop()
    
    return result


def print_function_call_trace(n):
 
    # Prints the trace of function calls for computing factorial
    
    a_stack = StackUsingList()
    factorial(n, a_stack)         # The stack traces the function calls
    
    print("The size of the stack is :", a_stack.size())
    
    print(f"Function call trace for factorial({n}):")
    
    
    for i in range(a_stack.size()):
        factorial_call = a_stack.items[i]
        print(factorial_call)

# Testing the function :

stack = StackUsingList()
print_function_call_trace(5)

# Output:
# Function call trace for factorial(5):
#          factorial(0)
#        factorial(1)
#      factorial(2)
#    factorial(3)
#  factorial(4)
#factorial(5)


# In[ ]:





# **Bonus**
# Implement stack using linked list examples provided in the lecture notes.
# 
# Learn how stack can be implemented using linkedlist by going through this visualization website: https://www.cs.usfca.edu/~galles/visualization/StackLL.html
