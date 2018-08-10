# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:31:30 2018

@author: disiz
"""
"""
-Session 2
-Assignment TWO
"""
##assignmnet 2 question 1
print("*/ assignment 2 output 1/*")
#asking user for inputting values
x1,x2,x3,x4,x5,x6=input("enter 6 values seperated by comma:").split(',')
generated_list=[x1,x2,x3,x4,x5,x6]
print(generated_list)
print("-"*100)
print('\n')
"""
-Session 2
-Assignment TWO
"""
##assignmnet 2 question 2
print("*/ assignment 2 output 2/*")
# defining shaping function
def shaping(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print('\r')
    for i in range(n,0,-1):
        for j in range(i-1):
            print("*",end=" ")
        print('\r')
shaping(5)
print("-"*100)
print('\n')
"""
-Session 2
-Assignment TWO
"""
##assignmnet 2 question 3
print("*/ assignment 2 output 3/*")
#asking user a question
str_inp=input("what is your favorite vegetable:")
print("in reverse order is:",str_inp[::-1])
print("-"*100)
print('\n')

"""
-Session 2
-Assignment TWO
"""
##assignmnet 2 question 4
print("*/ assignment 2 output 4/*")
print("WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a SOVEREIGN,\n\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t  and to secure to all its citizens")
print("-"*100)
print('\n')
print("End of assignment")