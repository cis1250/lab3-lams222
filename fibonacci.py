#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)

# Prompt the user for the number of terms.
user_input = input ("How many terms of the Fibonacci sequence do you want?")

# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

if user_input.isdigit():
  n_terms = int(user_input) #Turns string into integer
  if n_terms > 0: #Ensures positive values 
    a, b = 0, 1
    for i in range (n_terms):
        print (a, end=" ")
        a, b = b, a + b
    print ()
  else:
      print ("Please enter a positive integer")
else:
  print ("Please enter a positive integer")
