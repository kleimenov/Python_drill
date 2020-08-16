# 1) Let's say we have a number, num. 
# Find the number of values of n such that: there exists n consecutive positive values that sum up to num. 
# A positive number is > 0. n can also be 1.

def consecutive_sum(num):
    '''
    '''
    cnt, length = 1, 1
    
    while(length * (length + 1) < 2 * num): 
        a = (1 * num - (length * (length + 1) ) / 2) / (length + 1) 
        if (a - int(a) == 0): 
            cnt += 1
        length += 1
    return cnt 

# 2) My friend John likes to go to the cinema. He can choose between system A and system B.
# System A : he buys a ticket (15 dollars) every time
# System B : he buys a card (500 dollars) 
# and a first ticket for 0.90 times the ticket price, then for each additional ticket 
# he pays 0.90 times the price paid for the previous ticket.
# The function movie has 3 parameters: card (price of the card), ticket (normal price of a ticket), 
# perc (fraction of what he paid for the previous ticket) 
# and returns the first n such that ceil(price of System B) < price of System A.

import math
def movie(card, ticket, perc):
    '''
    '''
    ticket_mod = ticket
    full_price = 0
    cnt = 0
    
    while full_price - math.ceil(card) <= 0:
            ticket_mod *= perc
            card += (ticket_mod)
            full_price += ticket
            cnt = cnt + 1      

    return cnt

# 3) You must implement a function maxDiff that return the difference 
# between the biggest and the smallest value in a list(lst) received as parameter.
# The list(lst) contains integers, that means it may contain some negative numbers.
# If the list is empty or contains a single element, return 0.

def max_diff(lst):
    '''
    '''
    while lst:
        return max(lst) - min(lst)
    return 0