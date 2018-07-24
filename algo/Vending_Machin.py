"""
	Purpose: To find the Fewest Notes to be returned
	for Vending Machine
	@author Nikhil Patil
"""
from utility import *
class Vending_Machin:
	x = utility()
	i = 0
	notes = [1000,500,100,50,20,10,5,2,1]
	amount = int(input("enter the amount\n"))
	x.vendingMachin(notes,amount,i)