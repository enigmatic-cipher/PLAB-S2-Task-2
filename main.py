"""
Given an integer list as input. Create two functions named power4 and power5 taking an integer n as input and printing 4th power and 5th power of their respective input.
{3,5,8}
"""

def fourth_power(n):
  return n*n*n*n

def fifth_power(n):
  return n*n*n*n*n

num = int(input("Enter Number: "))
print(f"Fouth power of {num}: {fourth_power(num)}")
print(f"Fifth power of {num}: {fifth_power(num)}")
