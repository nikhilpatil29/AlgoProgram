"""
	Purpose: To convert Temperature from Fahrenheit to Celsius
	vice versa.
	@author Nikhil Patil
"""
class TemperaturConversion:
	celciusToFarenheit = int(input("Enter the temperature in Celsius:"))

	fareheitTocelcius = int(input("Enter the temperature in fareheit:"))

	convrt1=(celciusToFarenheit*9/5)+32

	convrt2=(fareheitTocelcius-32) * 5/9

	print convrt1," \n",convrt2