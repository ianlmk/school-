#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
  
  string input;
  string first;
  string middle;

  int int_a;
  int int_b;

  char char_a;
  char char_b;

  cout << "Enter some shit here: " << endl;
  getline(cin,input,',') >> first >> middle;
  cout << "The shit you said: \"" << input<< "\"" << middle << first << endl; 
  
  return 0;



}
