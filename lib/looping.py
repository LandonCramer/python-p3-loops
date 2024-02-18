#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    else:
        print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
   return [int * int for int in int_list]
print(square_integers([1,2,3,4,5]))

def fizzbuzz():
    for i in range(1,101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
fizzbuzz()