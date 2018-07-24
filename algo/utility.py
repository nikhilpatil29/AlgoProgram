class utility:
	# -------------------Algorithm Prorgram------------------

	"""
	1. An Anagram Detection Example
		@param str1
		@param str2

	"""
	def isAnagram(str1, str2):

		if (len(str1) == len(str2)):
			i = 0
			flag = 0
			while i < len(str1):
				flag = 0
				j = 0
				while j < len(str1):
					if (str1[i] == str2[j]):
						# print letter
						flag = 1
					j = j + 1
				i = i + 1
			if (flag == 1):
				print "String are anagram"
			else:
				print "String are not anagram"
		else:
			print "string are not equal"


	# 2 Prime number between 0 - 1000
	# @param number
	# @return
	def prime(self,number):
		j = 2
		flag = 0
		while j < number:
			if number%j == 0:
				flag = 1
			j +=1
		if flag == 0:
			return True
		else:
			return False

	# 3. Prime anagrams and palindromes
	# @param range1
	def palPrime(self,range1):
		index = 2
		while index < range1:
			if self.prime(index) and self.palindrome(index):
				print index," is Palindrome and Prime"
			index +=1

	# Function to calculate Palindrome
	# @param number
	# @return
	def palindrome(self,number):
		rem =0
		sum1 = 0
		temp = number
		while temp > 0:

			rem = temp%10
					# print rem
			sum1 = sum1 *10 + rem
					# print sum1
			temp = temp / 10
					# print i
		if number == sum1:
			return True
		else:
			return False


	# 5.Program to find your number using binary search
	# @param low
	# @param high
	def findPower(self,low,high):
		if low==high:
			print "your number is ",low
			print "your intermediate number is ",(low-1)," and ",(high+1)
			return;
		mid = (low+high)/2;
		
		
		print "press 1: ",low," - ",mid
		print "press 2: ",mid+1," - ",high
		
		choice = int(raw_input("enter the choice \n"))
		
		if (choice == 1):
			self.findPower(low, mid)
		elif(choice == 2):
			self.findPower(mid+1, high)
		else:
			print "you entered a wrong choice "
	

	# 8.Program for Bubble Sort
	# @param sortList
	# return
	def bubbleSort(self,sortList):
		temp = 0
		for i in range(0,len(sortList)-1):
			
			for j in range(0,len(sortList)-1-i):
				
				if sortList[j] > sortList[j+1]:
					temp = sortList[j]
					sortList[j] = sortList[j+1]
					sortList[j+1] = temp
		return sortList


	# 7.Program for Insertion Sort
	# param array
	def insertionsort(self,array):
		for index in range(1,len(array)):
			value = array[index]
			i = index - 1
			while i >= 0:
				if value < array[i]:
					array[i+1] = array[i]
					array[i] = value
					i = i-1
				else:
					break
		print("sorted String is")
		print array


	# 14.sqrt of non-negative Number
	# @param number
	def sqrtFunction(self,number):
		t = number;
		epsilon = 1e-15;
		
		while((t-number/t) > epsilon*t):
			t=(number/t +t)/2;
		print "Square root of ",number,"is ",t,"\n";


	# 10.Function to Find the Fewest Notes to be
	# returned for Vending Machine
	# @param notes
	# @param amount
	# @param i
	def vendingMachin(self,notes,amount,i):
		total = 0
		if amount == 0:
			return
		else:
			if amount >= notes[i]:

				calculatedNotes = amount//notes[i]
			
				rem = amount % notes[i]
	
				amount = rem 
			
				total = total +calculatedNotes
		
				print notes[i]," notes------>",calculatedNotes
			i +=1
			self.vendingMachin(notes,amount,i)

	# 15. Decimal to Binary conversion
	# @param number
	# return
	def toBinary(self,number):
		index = 0
		array = []
		arr = []
		while number > 0:
			array.append(str(number % 2))
			number = number/2
			index += 1
		for i in range(len(array)):
			arr.append(str(array.pop()))
		while len(arr) < 8:
			arr.insert(0,str(0))
		return arr

	# 16.Binary.java ---> convert decimal to binary swap
	# nibbles and fins new decimal number
	# @param array
	# return
	def swap(self,array):
		temp1 = array[0:4]
		temp2 = array[4:9]
		str1 = temp2
		str2 = temp1
		return str1 + str2

	# Function  to convert binary to Decimal
	# @param result2
	# return
	def convertToDecimal(self,result2):
		decimal = 0;
		swap = []
		for i in result2:
			swap.append(int(i))
		# print swap
		i = 0
		
		j = len(swap)-1
		print "len ",j
		while(j>=0):
			decimal = decimal + (swap[i] * (2**j))
			j-=1
			i += 1
		# print swap[i]
			
		return decimal