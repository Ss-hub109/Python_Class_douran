# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:44:26 2020

@author: Sadaf
"""

# add
def add(num1, num2): 
    return num1 + num2 

# subtract
def subtract(num1, num2): 
    return num1 - num2 

# multiply
def multiply(num1, num2): 
    return num1 * num2 

# divide
def divide(num1, num2): 
    return num1 / num2 

def calculate():
    print("Operations:\n" 
            "1. add\n" 
            "2. subtract\n" 
            "3. multiply\n" 
            "4. divide\n") 
    # Select operation  
    select = int(input("Select operations:")) 
    num1 = int(input("Enter number1: ")) 
    num2 = int(input("Enter number2: "))
    if select == 1: 
        print(num1, "+", num2, "=", 
                    add(num1, num2)) 
  
    elif select == 2: 
        print(num1, "-", num2, "=", 
                    subtract(num1, num2)) 
  
    elif select == 3: 
        print(num1, "*", num2, "=", 
                    multiply(num1, num2)) 
  
    elif select == 4: 
        if num2 != 0:
              print(num1, "/", num2, "=", 
                        divide(num1, num2)) 
        elif num2==0:
              print("Invalid Operation")
    else: 
        print("Invalid input") 
        
calculate()