"""
	Purpose: To read an integer as an Input,convert to Binary
	using toBinary function and perform swapping of nibbles.
	@author Nikhil Patil
"""
from utility import *
class Binary:

	x = utility()

	number = input("enter the number\n")
	result1 = x.toBinary(number)
	print result1,"\n"
	result2 = x.swap(result1)
	print " after swapning a digits \n",result2

	result3 = x.convertToDecimal(result2)
	print "after converting a binary to decimal \n",result3
	