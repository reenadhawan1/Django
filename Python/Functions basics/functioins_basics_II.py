# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  
# For example countDown(5) should return [5,4,3,2,1,0].

def countdown(num):
    arr = []
    for i in range(num,-1,-1):
        arr.append(i)
    return arr
# answer = countdown(50)
# print(answer)    
################################################################
# Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.

def printReturn(arr):
    if len(arr) != 2:
        return
    else:
        print(arr[0])
        return arr[-1]
# answer = printReturn([1,3])
# print(answer) 
################################################################
# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

def firstPlusLength(arr):
    if len(arr) == 0:
        return
    x = arr[0]+len(arr)
    return x
# answer = firstPlusLength([1,2,2,2,3])
# print(answer) 
################################################################
# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  
# Print how many values this is.If the array is only element long, have the function return False

def valGreterSec(arr):
    newArr = []
    cnt = 0
    for i in range(len(arr)):
        if arr[i] > arr[1]:
            newArr.append(arr[i])
            cnt += 1
    return newArr
# answer = valGreterSec([1,2,5,2,3])
# print(answer) 
################################################################
# This Length, That Value - Given two numbers, return array of length num1 with each value num2.  Print "Jinx!" if they are same.

def thisLenThatVal(x,y):
    if x == y:
        print("Jinx!")
    arr = []
    for i in range(x):
        arr.append(y)
    return arr
# answer = thisLenThatVal(5,2)
# print(answer) 