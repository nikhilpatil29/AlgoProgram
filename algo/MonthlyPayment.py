"""
	Purpose: To calculate monthly payment
	@author Nikhil Patil
"""
class MonthlyPayment:

		p1 = int(input("enter a p value"))
		y1 = int(input("enter a y value"))
		r1 = int(input("enter a r value"))

		r=r1/(12*100)
		n=12*y1
		MP=(p1*r1)/(1-((1+r1)**(-n)))
		print "The Monthly income is: ",MP,"Rs"
