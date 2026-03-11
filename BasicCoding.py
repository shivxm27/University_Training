#-------list---------


mylist = ["Shivam" , "Arnav" , "Dhruv" , 27 , 60.25 ]

# print(mylist)
# print(type(list))


# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])


# print(mylist[2:5])
# print(mylist[1:4:2])
# print(mylist[-1])



#-------------Code no 2--------------

# mylist.append('Sid')
# mylist.append(92)

# print(mylist)



#-----------3----------

# mylist.insert(4 , 202.12)
# print(mylist)

#------------4-----------


# mylist.remove('Dhruv')
# print(mylist)



#------------5-----------

# newList = mylist.copy()
# print("Old List:",mylist)
# print("New List:",newList)




#------------6 : Nested List------------


# nestList = [["Shivam" , 19] ,
#             ["Shubham" , 23] , 
#             ["Pangul" , 20]]

# print("Example of MultiDimensional List : ")
# print(nestList)



# print(nestList[0][0])
# print(nestList[0][1])
# print(nestList[1][0])
# print(nestList[1][1])
# print(nestList[2][0])
# print(nestList[2][1])





#-------------------7------------------


# list1 = ["Shivam" , "Mandlekar"]
# print(list1 * 2) #Will print 2 times



# list2 = [50 , 25 , 12]
# print(list1 + list2)






#-------------8---------------------


# listNew = [50 , 25 , 12 , "Shivam"]
# print(listNew)
# del listNew[1]

# print(listNew)



#------------------9---------------

# listNew = [50 , 25 , 12 , "Shivam"]
# print(listNew)





# listNew.clear()
# print(listNew)


#--------------------10------------------

# name = "Shivam"
# print(name)

# myName = list(name) # -> This is called Typecasting
# print(myName)



#--------------------11 Sorting Example------------------
# myList = [44,23,73,13,62,13]
# myList.sort() # -> Will sort in Ascending Order
# print(myList)




# myList.sort(reverse= True) # -> This will sort in desending Order
# print(myList)


# #While sorting - the list should contain homogeneous elements 


#--------------------12------------------
# testAddress1 = 10
# testAddress2 = 10
# testAddress3 = 20


# print(id(testAddress1)) #-> ID function is used to return the address of variable
# print(id(testAddress2))
# print(id(testAddress3))


#IF 2 values are same - no new memory is created the same value is used

#--------------------13 Aliasing------------------


# myList = [12,42,69,1,28,12]

# newList = myList


# print(id(myList))
# print(id(newList))


#--------------------14 Operators for Looping------------------
#Two types of operators are introduced in Python - Memebership ('in' operator) and Identity



# name = "Shivam"
# print('Z' in name)
# print('Z' not in name)



#--------------------15 Looping-----------------
# for i in range(1 , 11):
#     for j in range(1 , 21):
    
#         k = i * j
#         print(k, end=""  ) # -> Table of two
#     print()
    

#--------------------16 simple if else------------------
#WAP to check whether a user input digit is positive , negative or zero
# num = int(input("Enter Any Number :"))
# if num > 0:
#         print("Number is Positive")
# if num == 0:
#         print("Number is Zero")
# if num < 0:
#         print("Number is Negative")
        

#--------------------17------------------
#WAP to accept the days of the week and check the working or weekend


# day = str(input("Enter any day of the Week : ")).capitalize()
# if day in ["SATURDAY" , "SUNDAY"]:
#         print("Yay , it is a Weekend")
# else:
#         print("It is a Working day.")



#--------------------18------------------

#WAP to accept three paper marks and calculate total , percentage and if percentage
# is >= 60 then student is elgible for placement 



# marks1 = float(input("Enter Paper 1's Marks (out of 100): "))
# marks2 = float(input("Enter Paper 2's Marks (out of 100): "))
# marks3 = float(input("Enter Paper 3's Marks (out of 100): "))



# total = marks1 + marks2 + marks3
# percent =  (total / 300 ) * 100


# print("Total marks out of 300 are : ",total)
# print("Percentage scored by Student is : ",percent)

# if percent >= 60:
#         print("Student is eligible for placement.")
# else:
#         print("Not eligible.")
#--------------------19------------------


#WAP to accept 5 different value in 5 different variables and check maximum value
#by using simple IF statements only

val1 = int(input("Enter 1st Value : "))
val2 = int(input("Enter 2nd Value : "))
val3 = int(input("Enter 3rd Value : "))
val4 = int(input("Enter 4th Value : "))
val5 = int(input("Enter 5th Value : "))


if val1 > val2 and val1 > val3 and val1 > val4 and val1 > val5:
        print("Maximum value is :" ,val1)
if val2 > val1 and val2 > val3 and val2 > val4 and val2 > val5:
        print("Maximum value is :", val2)

if val3 > val1 and val3 > val2 and val3 > val4 and val3 > val5:
        print("Maximum value is :", val3)

if val4 > val1 and val4 > val2 and val4 > val3 and val4 > val5:
        print("Maximum value is :", val4)

if val5 > val1 and val5 > val2 and val5 > val3 and val5 > val4:
        print("Maximum value is :", val5)