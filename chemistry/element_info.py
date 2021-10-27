#!/bin/bash python
"""
Created by: Ian LaMotte-Kerr
"""

import pandas as pd
import argparse
from tabulate import tabulate
##############################################################
# format of the data held in the periodic table to work with #
##############################################################
"""
columns=["AtomicNumber","Element","Symbol","AtomicMass","NumberofNeutrons","NumberofProtons","NumberofElectrons","Period","Group","Phase","Radioactive","Natural","Metal","Nonmetal","Metalloid","Type","AtomicRadius","Electronegativity","FirstIonization","Density","MeltingPoint","BoilingPoint","NumberOfIsotopes","Discoverer","Year","SpecificHeat","NumberofShells","NumberofValence"]
"""
table_file="periodic_table"
element_df = pd.read_csv(table_file,header=0)
element_dataframe=element_df.astype(str)

def get_args(argv=None):
  parser = argparse.ArgumentParser(description='Generate element information from a verbose periodic table')
  parser.add_argument('-nu', metavar='nu', type=str, help='Enter an atomic number')
  parser.add_argument('-na', metavar='na', type=str, help='Enter an element name')
  return parser.parse_args(argv)

def get_element_data(category, string):
    data = element_dataframe.loc[element_dataframe[category] == string ]
    print (tabulate(data, headers ='keys', tablefmt ='psql'))

def get_column(string):
  columns=element_dataframe.head()
  for x in columns: 
    exists=element_dataframe.loc[element_dataframe[x] == string]
    if exists.empty != True: 
      column=x
  return column

def element_dict():
  element_obj=element_dataframe.to_dict(orient='records')
  return element_obj

def main():
  argvals=None
  args=get_args(argvals)
  name=args.na
  number=args.nu
  #element_dict()
  if name != "" and name != None:
    string = name
    category = get_column(string)
  if number != "" and number != None:
    string = number  
    category = 'atomic number'
    
  get_element_data(category,string)

if __name__ =='__main__':
  main()
