# 6.Program for binary search the word from wordlist
# @author Nikhil Patil
class BinarySearch:

	# Function for BinarySearch word list from file
	# @param ele
	# return
	def binarySearch(array,ele):
		
		first = 0
		last = len(array)

		while first < last:
			mid = (first+last)/2
			if(ele < array[mid]):
				last = mid
			elif(ele > array[mid]):
				first = mid+1
			else:
				return mid
		return -1

	f = open('demo.txt')
	mylist = []
	mylist = f.read().split(" ")
	print mylist


	item = raw_input("enter the word which you want to search\n")
	result = binarySearch(mylist, item)
	if result != -1:
		print "Element is found at ",result+1," position" 
	else:
		print "Element is not present in the list"