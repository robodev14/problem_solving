"""
FizzBuzz program 
Problem: Iterate 1 to 50.
Print "Fizz" for multiples of 3
Print "Buzz" for multiples of 5
Print "FizzBuzz" for multiples of both 3 and 5
"""

def run_fizzbuzz():
  for FizzBuzz in range(50):
    if FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
      print("FizzBuzz")
      continue
    elif FizzBuzz % 3 == 0:
      print("Fizz")
      continue
    elif FizzBuzz % 5 == 0:
      print("Buzz")
      continue
    print(FizzBuzz)
    
    
run_fizzbuzz()