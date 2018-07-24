"""
	Purpose: Take a range of 0 - 1000 Numbers and find the Prime
	numbers in that range.

	@author Nikhil Patil
"""
from utility import *
class Range_Prime:

	x = utility()
 	number = int(raw_input("enter the range between 1 to 1000\n"))
 	print "\palindrome number is\n"
 	i = 2
 	while i < number:
	 	result = x.prime(i)
	 	
	 	if result == True:
	 		print i," is prime number"
	 	else:
	 		pass
	 	i += 1


