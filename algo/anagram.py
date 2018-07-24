'''
 Purpose: An Anagram Detection Example
 @author Nikhil Patil

 '''
from utility import *
class Anagram:

	obj = utility()
	st1 = raw_input("enter first string\n")
	st2 = raw_input("enter second string\n")

	obj.isAnagram(st1,st2)