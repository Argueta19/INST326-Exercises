"""A template for a python script deliverable for INST326.
Driver: Instructor Gabriel Cruz
Navigator: None
Assignment: Template INST326
Date: 1_24_21
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import sys
import argparse
import os
def determine_winner(p1, p2):
  #insert code and docstrings here
  pass
def main(player1_name, player2_name):
  #insert code and docstrings here
  pass
def parse_args(args_list):
  """Takes a list of strings from the command prompt and passes them through as
arguments
  Args:
  args_list (list) : the list of strings from the command prompt
  Returns:
  args (ArgumentParser)
  """
  #For the sake of readability it is important to insert comments all throughout.
  #Complicated operations get a few lines of comments before the operationscommence.
  #Non-obvious ones get comments at the end of the line.
  #For example:
  #This function uses the argparse module in order to parse command line arguments.
  parser = argparse.ArgumentParser() #Create an ArgumentParser object.
  #Then we will add arguments to this parser object.
  #In this case, we have a required positional argument.
  #Followed by an optional keyword argument which contains a default value.
  parser.add_argument('p1_name', type=str, help="Please enter Player1's Name")
  parser.add_argument('p2_name', type=str, help="Please enter Player2's Name")
  args = parser.parse_args(args_list) #We need to parse the list of command linearguments using this object.
  return args
if __name__ == "__main__":
  #If name == main statements are statements that basically ask:
  #Is the current script being run natively or as a module?
#It the script is being run as a module, the block of code under this will not beexecuted.
  #If the script is being run natively, the block of code below this will beexecuted.
  arguments = parse_args(sys.argv[1:]) #Pass in the list of command line argumentsto the parse_args function.
  #The returned object is an object with those command line arguments as attributesof an object.
  #We will pass both of these arguments into the main function.
  #Note that you do not need a main function, but you might find it helpfull.
  #You do want to make sure to have minimal code under the 'if __name__ =="__main__":' statement.
  main(arguments.p1_name, arguments.p2_name)