# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". 
# Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def biggieSize(arr):
    for i in range(0,len(arr),1):
        if arr[i] > 0:
            arr[i] = "big"
    return arr
# answer = biggieSize([1,2,-4,-8,6])
# print(answer)    
################################################################
# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. 
# Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to b a positive number).

def countPositives(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            cnt += 1
    arr[len(arr)-1] = cnt
    return arr
# answer = countPositives([1,2,-4,-8,6])
# print(answer)    
################################################################
# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  
# For example sumTotal([1,2,3,4]) should return 10

def sumTotal(arr):
    tot = 0
    for i in range(len(arr)):
        tot += arr[i]
    return tot
# answer = sumTotal([1,2,-4,-8,6])
# print(answer)    
################################################################
# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  
# For example multiples([1,2,3,4]) should return 2.5

def average(arr):
    tot = 0
    for i in range(len(arr)):
        tot += arr[i]
    avg = tot / len(arr)
    return avg
# answer = average([1,2,-4,-8,6])
# print(answer)    
################################################################
# Length - Create a function that takes an array as an argument and returns the length of the array.  
# For example length([1,2,3,4]) should return 4

def length(arr):
    l = 0
    for i in range(len(arr)):
        l += 1
    return l
# answer = length([1,2,-4,-8,6])
# print(answer)    
################################################################
# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  
# For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(arr):
    if len(arr) < 1:
        return False
    else:
        small = arr[0]
        for i in range(len(arr)):
            if arr[i] < small:
                small = arr[i]
    return small
# answer = minimum([1,2,-4,-8,6])
# print(answer)    
################################################################
# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  
# For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -3.

def maximum(arr):
    if len(arr) < 1:
        return False
    else:
        big = arr[0]
        for i in range(len(arr)):
            if arr[i] > big:
                big = arr[i]
    return big
# answer = maximum([1,2,-4,-8,6])
# print(answer)  
################################################################
# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def ult(arr):
    dic = {
        "sumTotal": sumTotal(arr),
        "average": average(arr),
        "minimum": minimum(arr),
        "maximum": maximum(arr),
        "length": length(arr),
    }
    return dic
# answer = ult([1,2,-4,-8,6])
# print(answer)  
################################################################
# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  
# For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def rev(arr):
    for i in range(int(len(arr)/2)):
        hold = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = hold
    return arr
# answer = rev([1,2,-4,-8,6])
# print(answer)  

