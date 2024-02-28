#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while(counter > 0):
        print(counter)
        counter -= 1
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    # code goes here!
    return [num * num for num in int_list]
square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz()