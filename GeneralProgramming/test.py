import random

def temperature_tuple(temp_in):
  return temp_in, (temp_in*9/5)+32

with open('temperature_checker.txt', 'w') as tc:
  for i in range(-40, 101):
    temperatures = temperature_tuple(i)

    tc.write(f'{temperatures[0]} {temperatures[1]:.2f}\r')

