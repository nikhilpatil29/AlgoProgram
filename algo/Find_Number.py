"""
	Purpose: Question to find your number.
	@author Nikhil Patil
"""
from utility import *
class Find_Number:
	x = utility()

	number = int(input("enter the number\n"))
	power = 2**number
	print power

	x.findPower(0,power)

