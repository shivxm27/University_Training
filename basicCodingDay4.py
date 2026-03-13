#---------------------------1--------------------------


# userName = " "
# password = ""

# while userName != "admin" and password != "hello":
#     userName = str(input("Enter Username : "))
#     password = str(input("Enter Password : "))
#     print("Incorrect Credentials - Try Again")
# print("Correct Credentials")







#---------------------------2 Sum of first N numbers w/ user input--------------------------

# n = int(input("Enter Number : "))
# sum = 0
# i = 1

# while i <= n:
#     sum = sum + i
#     i = i + 1


# print("The sum of first" , n ,"numbers is : ",sum)


#---------------------------3 Removing duplicate characters in a string--------------------------

# name = "prashant"
# result = ""

# for char in name:
#     if char not in result:
#         result = result + char


# print("Result is : ",result)








#---------------------------4 Reversing String using loop--------------------------


# name = "prashant"

# revName = ""

# for char in name:
#     revName = char + revName

# print("Reversed String is : ",revName)

#---------------------------5--------------------------
# myCart = [10 , 20 , 200 , 300 , 800 , 60 , 700]

# for i in myCart:
#     if i > 400:
#         print("This is my purchased cart item")
#         continue
#     print(i)



#---------------------------6WAP To check whether a string is pallindrom--------------------------
# pallinStr = str(input("Enter String : "))

# revStr = ""

# for char in pallinStr:
#     revStr = char + revStr

# if pallinStr == revStr:
#     print("The Given String " ,pallinStr," is a pallindrome.")
# else:
#     print("Not a pallindrome.")



# #alt approach ->

# if pallinStr == pallinStr[::1]:
#     print("It is a pallindrome")
# else:
#     print("Not a pallindrome")




#---------------------------7 wap to check for a anagram--------------------------

# str1 = str(input("Enter First String : "))
# str2 = str(input("Enter Second String : "))


# str1 = str1.lower()
# str2 = str2.lower()

# if sorted(str1) == sorted(str2):
#     print("The 2 strings are Anagrams.")
# else:
#     print("The 2 strings are NOT Anagrams.")

#---------------------------8  Update and Remove key value pairs from a dict--------------------------



# myDict = {
#     "Name" : "Shivam",
#     "Roll No" : 22 ,
#     "City" : "Ngp",
#     "Age" : 19
# }
# print(myDict)



# myDict.update({"Uni" : "RBU"})
# print(myDict)





# myDict.pop("Age")
# print(myDict)







# city = myDict.get("City")
# print(city)


# doesNotExist = myDict.get("Religion")
# print(Religion)

#---------------------------9 Nested FOR loops--------------------------
# -> we want to print 111 222 333 


# for i in range (1 , 4): #outerloop -> Represents Rows
#     for j in range(1 , 4): #innerloop -> Represents Columns
#         print(i , end=" ")
#     print("")




#---------------------------10--------------------------

# n = int(input("Enter the number of rows : "))

# for i in range( 1 , n + 1):
#     for j in range(1 + n + 1):
#         print(chr(64+i), end="") #ASCII
#     print()




#---------------------------11--------------------------
# n = int(input("Enter the number of rows : "))

# for i in range( 1 , n + 1):
#     for j in range(1 , n + 1):
#         print(n + 1 - i, end="") #ASCII
#     print()

#---------------------------12--------------------------

n = int(input("Enter the number of rows : "))

for i in range( 1 , n + 1):
    for j in range(1,  n + 2 - i ):
        print("*", end="")
    print()






