#  Purpose: To find the prime numbers that are Anagram and
# Palindrome
# @author Nikhil patil
from utility import *
class AnaAndPalin:

	x = utility()
	number = int(raw_input("enter the number between 1 to 1000\n"))
	print "\n Palindrom Number is :"
	x.palPrime(number)