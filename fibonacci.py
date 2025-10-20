#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
N = 0
while N <= 0:
  try:
    num_terms_str = input("Enter the number of Fibonacci terms you want: ")
# Validate that the input is a positive integer.
N = int(num_tearms_str)
if N <= 0:
  print("Please enter a positive integer")
# Use a for loop to print the Fibonacci sequence up to that many terms.
except ValueError
print("Invalide input. Please enter a whole number (integer)")
N = 0
a = 0
b = 1 

for i in range(N):
  result_string = result_string + str(a) + ""
temp = a + b 
a = b
b = temp
print(f"\nFibonacci Sequence for {N} terms:{result_string}")
# Your code doesn't run -3
