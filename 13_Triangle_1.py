#!usr/lib/python3
# author : 

# import os # library imports

# from input import list_input# local imports

# global variables

# classes

# functions

# driver_code
#      inputs
#      drivers

"""
comment for the function independent of anything

"""

# comments for the function triangle_1
def triangle_1(n, ch):
    for i in range(1, n + 1):
        print(ch * i)


def triangle_2(n, ch):
    for i in range(n, 0, -1):
        print (ch * i)


def triangle_3(n, ch):
    for i in range(n):
        for j in range(1, i - 1):
            if j == 1 or j == i - 2:
                print(ch, end = " ")
            else:
                print(" ", end = " ")
        print("\n")
        if i == n-1:
            for _ in range(0, i - 2):
                print(ch + " ", end = " ")
    print ("\n")


def right_triangle(n, ch):
    for i in range(1, n + 1):
        print(' ' * (n -i ) + ch * i)


def top_triangle(n, ch):
    for i in range(0, n):
        print((n - i) * ch)


def bottom_triangle(n, ch):
    for i in range (n, 0, -1):
        print (' ' * (n-i) + i * ch)


'''
  *
 ***
*****

'''

def isosceles_triangle(n, ch):
    for i in range(1, n+1):
        print(' ' * (n - i) + ((2 * i - 1) * ch) )

def right_isosceles_triangle(n, ch):
    for i in range (1, n + 1):
        print(ch * i)
    for i in range (1,n):
        print(ch * (n-i))

def right_left_isosceles_triangle(n, ch):
    for i in range (1, n + 1):
        print(ch * i + ' ' * (2 * n - 2 * i) + ch * i)
    for i in range (1,n):
        print(ch * (n-i)+' ' * 2 * i + ch * (n - i))

def shape_1(n, ch):
    isosceles_triangle(n, ch)
    for i in range(1, n + 1):
        print((' ' * n) + (ch * (n - i )) + (i * ' '))
    
def shape_2(n, ch):
    for i in range(1, n + 1):
        print(' ' * (n -i ) + ch * i)
    for i in range(n, 0, -1):
        print (' ' * n +ch * i)
def shape_3(n, ch):
    for i in range(1, n):
        print(' ' * (n -i ) + ch * i)
    print (ch * n * 2)
    for i in range(n - 1, 0, -1):
        print (' ' * n +ch * i)

'''
*********
**** ****
***   ***
**     **
*       *
**     **

'''

def square_1(n, ch):
    print (ch * (2 * n-1))
    for i in (1,n):
        print((ch * (n - i)) + (' ' * (2 * i -1)) + (ch * (n - i)))
    for i in (2, n):
        print((ch * i) + (' ' * ( 2 * i - 1)) + (ch * i) )
    print (ch * (2 * n-1))

n = int(input("Enter a number :"))
ch = input ("Enter a character :")

#triangle_1(n, ch)
#triangle_2(n,ch)
#triangle_3(n,ch)
#right_triangle(n, ch)
#top_triangle(n, ch)
# bottom_triangle(n, ch)
#isosceles_triangle(n, ch) 
#right_isosceles_triangle(n, ch)
right_left_isosceles_triangle (n, ch)
shape_1(n, ch)
shape_2(n, ch)
shape_3(n, ch)
#square_1(n, ch)


