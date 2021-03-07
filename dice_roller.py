#!/usr/bin/env python3
import random



def main():
  num_rolls = 2
  sum_rolls = 0
  for x in range(num_rolls):
    roll = random.randint(1, 6)
    if roll == 1:
      print(f'You rolled a {roll}; Critical Fail!')
    elif roll == 6:
      print(f'You rolled a {roll}; Critical Success!')
    else:
      print(f'You rolled a {roll}')
    sum_rolls += roll
  print(f'You have rolled a total of {sum_rolls}')

if __name__== "__main__":
  main()
