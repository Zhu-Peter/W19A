# write a function that takes in one number as an argument
# This function will:
# print "Fizz" if the number is divisible by 3
# print "Buzz" if the number is divisible by 5
# print "FizzBuzz" if the number is divisible by both 3 and 5
# The function should only ever print once per number!
# Create a list of random numbers with at least 15 numbers inside
# Run the function above for each number in your list.

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for num in test_list:
    fizzbuzz(num)