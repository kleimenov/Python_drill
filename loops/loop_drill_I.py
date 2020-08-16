#This I will solve different problems with loops.
#All problems I solved from codewars. I guess it is best way to 
#increase your Python skells and algorithms knowledge. 

#First set of solutions. In this file I've added just problems with difficult level 8 (eseast level)

#1) Build the function that will get array in input and return value that equal maximum 
#value in array + 1 as output. 

def next_num(arr):
    '''
    Function next_num() get array, sort it,
    and returns smallest unused number for 
    next new data item
    ex: if function get array like
    [1,2,3,4,5], function will return #5
    '''
    a = 0
    if len(arr) != 0:
        b = max(arr)+2 or 0
    else:
        b = 1
    for i in range(a, b):
        if i not in arr:
            next_min = i
            break
    return next_min

#2) In this simple exercise, you will build a program that takes a value, integer, 
#and returns a list of its multiples up to another value, limit. 
#If limit is a multiple of integer, it should be included as well. 
#There will only ever be positive integers passed into the function, not consisting of 0. 
#The limit will always be higher than the base.
#For example, if the parameters passed are (2, 6), 
#the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
#If you can, try writing it in only one line of code.

def find_multiples(integer, limit):
    '''
    Function get two parameters 'integer' and 'limit'.
    This parametrs are integers. Fanctions will return a list
    of integers that first value vill will be equal 'integer' parametr 
    and finish that will be equal 'limit' parametr, and each step equal 
    value of parametr 'integer'.
    '''
    n = 1
    return [x for x in range(integer,limit + n,integer)]


#3) Your task is to find the first element of an array that is not consecutive.
#By not consecutive we mean not exactly 1 larger than the previous element of the array.
#E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, 
#so that's the first non-consecutive number. If the whole array is consecutive then return null2.
#The array will always have at least 2 elements1 and all elements will be numbers. 
#The numbers will also all be unique and in ascending order. 
#The numbers could be positive or negative and the first non-consecutive could be either too!


def first_non_consecutive(arr): 
    '''
    Function get array and return
    non consecuetive number
    '''
    tmp = None
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != 1:
            tmp = arr[i]
            break
    return tmp


#4) Write the function that will remove the left-most duplicates 
# from a list of integers and return the result.

def solve(arr):
    '''
    Function get array and return just 
    unique values
    '''
    z = []

    for i in range(len(arr)-1,-1,-1):
        if arr[i] not in z:
            z.append(arr[i])
    return z[::-1]

