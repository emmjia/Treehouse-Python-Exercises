#Let's create a function that determines if a specific value is odd.
#Let's name the function is_odd and have it declare a single parameter.
#It should return True if the value is not divisible by 2.

def is_odd(value):
    if value % 2 == 1: 
        return True
    else:
        print(f"{value} is an even number, therefore not true")

value = int(input("Type a number: "))
is_odd(value)