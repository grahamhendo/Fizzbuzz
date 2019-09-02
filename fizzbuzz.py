# -*- coding: utf-8 -*-
"""
Spyder Editor

This code lists the numbers from 1 to 100.  If the number is divisible by 3
fizz is printed, if the number is divisible by 5 then buzz is printed.  If the
number is divisible by 3 and 5 then fizzbuzz is printed.
"""

for x in range(1, 101):
    fizz = x % 3
    buzz = x % 5
    if fizz == 0 and buzz == 0:
        print("fizzbuzz") 
    elif fizz == 0:
        print("fizz") 
    elif buzz == 0:  
        print("buzz") 
    else: print(x)
    