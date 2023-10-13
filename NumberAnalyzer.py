def check_odd_even(number):
  if number % 2 == 0:
    print(f'{number} is an even number')
  else:
    print(f'{number} is an odd number')

def get_factors(number):
  factors = []
  iteration_index = 1
  while iteration_index <= number:
    if number % iteration_index == 0:
      factors.append(iteration_index)
    iteration_index += 1
  print(f'The factors of {number} are: {factors}')
  return factors

def check_prime(number, factors):
  if len(factors) == 2:
    print(f'{number} is a prime number')
  else:
    print(f'{number} is not a prime number')

def analyze_number(number):
  check_odd_even(number)
  factors = get_factors(number)
  check_prime(number, factors)

print("Please input a positive whole number to analyze: ")

check = input()
check = int(check)

analyze_number(check)
