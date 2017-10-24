# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 00:46:48 2017

@author: Jonas
"""

# implementation of Fizzbuzz
# a countinggame
# if the number is divisible by 3 you say 'Fizz'
# if the number is divisible by 5 you say 'Buzz'
# if zhe number is divisible by both you say 'FizzBuzz'
# else you just say the number

def fizzbuzz( limit ) :
    rules = { 15 : 'Fizzbuzz',
               5 : 'Buzz',
               3 : 'Fizz'
             }
    for num in range( 1, limit + 1 ) :
        out = ''
        for rule in rules :
            if num % rule == 0 : out += rules[ rule ] ; break
        print( out ) if out != '' else print( num )
