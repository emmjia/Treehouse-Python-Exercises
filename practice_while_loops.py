name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops

question = input(f"Hello {name}, do you understand Python while loops?(yes/no)")


# TODO: Write a while statement that checks if the user doesn't understand while loops

while question != 'yes':
    print("Perhaps you need a refresher. Allow me to explain.")

# TODO: Since the user doesn't understand while loops, let's explain them.

    print("A while loop is a line or block of code that is allowed to run on repeat as long as the condition provided is met.")

# TODO: Ask the user again, by name, if they understand while loops.

    question = input(f"So {name} do you now understand while loops?(yes/no)")
  
# TODO: Outside the while loop, congratulate the user for understanding while loops

print("Great!, I'm glad that you understand while loops.")
 
