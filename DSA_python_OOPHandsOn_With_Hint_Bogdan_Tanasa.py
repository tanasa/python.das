#!/usr/bin/env python
# coding: utf-8

# ### **Problem 1: Creating a Student Management System**
# Design a Student class to manage student information. The class should have attributes for student name, age, and a list of courses they are enrolled in. Implement methods to add a new course, drop a course, and display the student's details.
# 
# Skeleton Code:



class Student:

    def __init__(self, name, age):
        # Initializing student name, age, and an empty list of courses
        self.name = name
        self.age = age
        self.courses = []

    def add_course(self, course):
        # Adding a course to the student's list of courses
        self.courses.append(course)

    def drop_course(self, course):
        # Checking if the course is in the list before removing it
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"Course '{course}' not found.")

    def display_details(self):
                   
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print("Courses enrolled :")
        if self.courses: 
            for a_course in self.courses:
                print(f"- {a_course}")        
        else: 
            print(f"The Student, {self.name}, did not enroll in any class") 
         

# Example Usage:

student1 = Student("John Doe", 20)
student1.add_course("Math")
student1.add_course("History")
student1.drop_course("Science")  # This will trigger the 'not found' message
student1.display_details()


# ### **Problem 2: Implementing a Basic Shape Hierarchy**
# 
# Create a Shape class with attributes for color and a method to calculate the area (initialize it as 0). Then, create subclasses Circle and Rectangle that inherit from Shape. Implement the area calculation method for each subclass.
# 
# Skeleton Code:



import math

class Shape:
    def __init__(self, color):
        self.color = color

    def calculate_area(self):
        """Returns 0 for the area of a non-defined shape."""
        self.area = 0
        return self.area

class Circle(Shape):
    def __init__(self, color, radius):
        
        # Initialize color using the superclass constructor
        super().__init__(color)
        #  Using super() allows for a clearer structure in the inheritance hierarchy
        # self.color = color
        
        # Implement the constructor to initialize radius
        self.radius = radius

    def calculate_area(self):
        
        # Implement the method to calculate the area of the circle
        self.area = math.pi * (self.radius ** 2)
        print(f"Area of Circle: {round(self.area, 2)}") 


class Rectangle(Shape):
    def __init__(self, color, width, height):
        
        # Initialize color using the superclass constructor
        super().__init__(color)
        # Using super() allows for a clearer structure in the inheritance hierarchy
        # self.color = color
            
        # Implement the constructor to initialize width and height
        self.width = width
        self.height = height

    def calculate_area(self):
        
        # Implement the method to calculate the area of the rectangle
        self.area = self.height * self.width
        print(f"Area of Rectangle: {round(self.area, 2)}")


# Example Usage:

circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)
circle.calculate_area()
rectangle.calculate_area()


# ### **Problem 3: Implementing a Simple Banking System with Inheritance**
# 
# Create a BankAccount class with attributes for account number and balance. Implement methods to deposit and withdraw money. Then, create subclasses SavingsAccount and CurrentAccount that inherit from BankAccount. Implement additional features like an interest calculation for SavingsAccount and overdraft limit for CurrentAccount.
# 
# Skeleton Code:


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount:.2f}. The new balance is: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive. Please enter the amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.balance:
                print("Insufficient funds.")
            else:
                self.balance -= amount
                print(f"Withdrawn: {amount:.2f}. The new balance is: {self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive. Please enter the amount.")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance) 
        self.interest_rate = interest_rate

    def calculate_interest(self, deposit_amount):
        # First, deposit the amount to the balance
        self.deposit(deposit_amount)
        # Then, calculate interest on the new balance
        interest = self.balance * self.interest_rate
        self.balance += interest  
        print(f"The interest earned is: {interest:.2f}. The new balance is: {self.balance:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount > (self.balance + self.overdraft_limit):
                print("The withdrawal exceeds the overdraft limit.")
            else:
                self.balance -= amount
                print(f"Withdrawn: {amount:.2f}. The new balance is: {self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive. Please enter the amount.")


# Example Usage
savings_account = SavingsAccount("SA123", 5000, 0.05)
savings_account.calculate_interest(1000)  # Deposit and then calculate interest
print(f"Savings Account Balance: {savings_account.balance:.2f}")

current_account = CurrentAccount("CA456", 3000, 2000)
current_account.withdraw(3500)  # Allowed due to overdraft
print(f"Current Account Balance: {current_account.balance:.2f}")





