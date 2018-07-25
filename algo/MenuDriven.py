'''
 Purpose: Program to perform all sorting operation like
 insertion,bubble etc
 @author Nikhil Patil

 '''
from utility import *
class MenuDriven:

    x = utility()
    choice = 0
    while 1:
        print "Menu : "
        print "1. binarySearch method for integer"
        print "2. binarySearch method for String"
        print "3. insertionSort method for integer"
        print "4. insertionSort method for String"
        print "5. bubbleSort method for integer"
        print "6. bubbleSort method for String"
        print "7.Exit"

        choice = int(input("\nenter your choice\n"))
        if choice == 1:
            numList = [1,3,6,9,11,32,54,59,61]
            print numList
            ele = input("enter the element to search")
            pos = x.binarySearchInteger(ele,numList)
            if (pos != -1):
                print ele ," is found at " ,(pos + 1)," position"
            else:
                print("element not found")

        elif choice == 2:
            numList = ['a','b','c','d','e','f','g']
            print numList
            ele = raw_input("enter the element to search")
            pos = x.binarySearchString(ele,numList)
            if (pos != -1):
                print ele ," is found at " ,(pos + 1)," position"
            else:
                print("element not found")
        elif choice == 3:
            numList = [10, 15, 14, 13, 19, 8, 4, 33]
            print numList
            array1 = x.insertionSortInteger(numList)
            print"Sorted Insertion Sort Array : ",array1

        elif choice == 4:
            array = ["nikhil", "kunal", "zeeshan", "amar"]
            print array
            array1 = x.insertionSortString(array)
            print"Sorted Insertion Sort Array : ",array1

        elif choice == 5:
            numList = [10, 15, 14, 13, 19, 8, 4, 33]
            print "list before sort"
            print numList, "\n"

            print "list after sort"
            print(x.bubbleSort(numList))

        elif choice == 6:
            array = ["nikhil","kunal","zeeshan","amar"]
            print("Sorted Bubble Sort Array : ")
            print array
            print("Sorted Bubble Sort Array : ")
            x.bubbleSortString(array)
        else:
            exit(0)



        #
        #
        #
        # insertionSortString(str1, size)
        # print("Sorted Insertion Sort Array : ")
        # printStringArray(str1, size)
        # break


