#!/bin/bash python

import pandas as pd
import argparse

table_file="periodic_table_v1.1.csv"

def get_args(argv=None):
  parser = argparse.ArgumentParser(description='Generate element information from a verbose periodic table')
  parser.add_argument('-nu', metavar='nu', type=int, help='Enter an atomic number')
  parser.add_argument('-na', metavar='na', type=str, help='Enter an element name')
  return parser.parse_args(argv)

def get_element_data(name,number,column):
  element_dataframe = pd.read_csv(table_file,header=0)

  print(element_dataframe.loc[element_dataframe[column] == name ])

def main():
  argvals=None
  args=get_args(argvals)
  name=args.na
  number=args.nu
  print(name, number)
  if name != "":
    column = 'Element'
  if number != "" and column == None:
    column = 'AtomicNumber'

  get_element_data(name,number,column)

if __name__ =='__main__':
  main()
