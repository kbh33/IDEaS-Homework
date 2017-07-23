# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 08:55:05 2017

@author: kirthana hampapur
"""
## Problem 1

SumOfNumbers = 0
for num in range(1000):
    if (num % 3 == 0) or (num % 5 == 0):
        SumOfNumbers = SumOfNumbers + num
print("The required sum of the numbers is: "+repr(SumOfNumbers))


# Problem 2

NumberSum = 2
FibNumOld = 1
FibNumNew = 2
while (FibNumOld <= 4000000) and (FibNumNew <= 4000000):
    temp = FibNumNew
    FibNumNew = FibNumNew + FibNumOld
    FibNumOld = temp
    if FibNumNew % 2 == 0:
        NumberSum = NumberSum + FibNumNew
print("The required sum of even Fibonacci numbers below 4 million is: "+repr(NumberSum))    


## Problem 3

num = 600851475143 # the number of interest
divisor = 2
factor = 0 # This is the greatest factor

while num >= divisor:
    if num % divisor == 0:
        num = num/divisor
        factor = divisor
        divisor = 2
    else:
        divisor += 1        
print("The greatest factor is: "+repr(factor))

## Problem 4

final = 0
for a in reversed(range(1,1000)):
    for b in reversed(range(1,1000)):
        product = a*b
        s = str(product)
        if (s[0:3] == s[3:6][::-1]) and (product > final):
            final = product
            finalA = a
            finalB = b
print("The largest six-digit palindrome is "+repr(final)+" which is the product of "+repr(finalA)+" and "+repr(finalB))


## Problem 5

num = 20 # The number required cannot be lesser than 20
check = False

while check == False:    
    if all(num % r == 0 for r in [11,13,14,16,17,18,19,20]): # other numbers are multiples of these numbers
        check = True
        break
    else:
        num = num + 20 # because the number has to be a multiple of 20
print("The smallest number that is an even multiple of all the numbers between 1 and 20 is: "+repr(num))
    

            