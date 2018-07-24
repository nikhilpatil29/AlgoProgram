"""
	Purpose: Print day of the week.
	@author Nikhil Patil
"""
class DayOfWeek:

	d = int(input("enter a  day value"))
	y = int(input("enter a year value"))
	m = int(input("enter a week value"))

	yo=(y-(14-m))/12
	print yo
			
	x=yo+(yo/4)-(yo/100)+(yo/400)
	print x
			
	mo=m+12*((14-m)/12)-2
	print mo
			
	doo=(((d+x+31*m)/12)%7)
	print doo