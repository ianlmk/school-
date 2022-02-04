#!/bin/bash python

import sys
import math

LOAD_FACTOR = 0.64
PI = math.pi


def main():

  print("Welcome to my gumball guesser program!\n")
  gumballRadius = float(input("Enter the radius of a gumball: "))
  containerSize = float(input("Enter the volume of your jar: "))
  gumballVolume = (4.0 / 3.0) * PI * gumballRadius**3
  gumballCount = round(((containerSize * LOAD_FACTOR) / gumballVolume),2);

  print("Estimate of gumballs in the jar: {}".format(gumballCount))
  print("Thank you for using my program")

    

if __name__ == "__main__":
  main()
