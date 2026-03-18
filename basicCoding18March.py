#------------1--------------

# userDef = str(input("Enter any String : "))
# checkCount = 0
# for ch in userDef:
#     if ch.isspace() or not ch.isalnum():
#         checkCount = checkCount + 1


# print("The Number of Whitespaces / Special Characters are :  ",checkCount)
#------------2 find the common element amongst three arrays --------------


# arr1 = [ 1, 7 ,3 ]
# arr2 = [ 2, 3 ,4 ]
# arr3 = [ 3, 4 ,5 ]


# for i in arr1:
#     if i in arr2 and arr3:
#         print(i)

#------------3 given in a array , move all zeros to end of element without changing order of the non zero elements--------------

# arr = [0 , 1 , 0 , 3 , 12]
# print(arr)

# for i in arr:
#     if i == 0 :
#         arr.remove(i)
#         arr.append(0)

# print(arr)

#------------4find the second largest element in a array --------------

# arr = [ 1 , 5, 1 , 8 , 10]
# print(arr)
# arr.sort()

# print(arr)
# print("Largest Element is : ", arr[-1])
# print("Second Largest Element is : ", arr[-2])

#------------5 WAP to calculate and return the sum of distances between the adjacnet numbers in a array of positive integers--------------
# arr = []
# arrLen = 0
# sumDist = 0
# arrLen = int(input("Enter Length of Array : "))

# for i in range(arrLen):
#     valueArr = int(input(f"Enter Element {i+1} : "))
#     arr.append(valueArr)

# for i in range(arrLen - 1):
#     sumDist += abs(arr[i] - arr[i+1])

# print("The Sum of distances between Adjacent elements is : ", sumDist)

#------------6HackerEarth - Roy and profile picture --------------



# L = int(input("Enter Length : "))
# N = int(input("Enter Number of Photos :"))

# for i in range(N):
#     W = int(input("Enter Width of Photo : "))
#     H = int(input("Enter Height of Photo : "))

#     if W < L or H < L:
#         print("Upload Another Photo.")
#     else:
#         if W == H:
#             print("Photo Accepted.")
#         else:
#             print("Crop the photo.")

#------------7Running a sum of 1d array - leetcode --------------


# arr = [ 1 , 2 , 3 , 4]
# print(arr)
# resultArr = []
# sum = 0

# for i in arr:
#     sum = sum + i 
#     resultArr.append(sum)


# print(resultArr)  
