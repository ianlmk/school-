#!/bin/bash python

import sys
import math


def main():

  serving_size = 3
  calories_per_cookie = 53

  print("Welcome to the Oreo calculator!")
  cookie_count = int(input("How many Oreos did you eat? "))

  total_calories = str(cookie_count * calories_per_cookie)
  total_servings = str(round((cookie_count / serving_size), 2))

  print("\n{} Oreos equals {} servings!".format(cookie_count,total_servings))
  print("You consumed {} calories.".format(total_calories))

if __name__ == "__main__":
  main()
