
#program for linear search

# arr = [3,4,5,8,-1,-100,10000,9,10000]
# n = int(input())
# counter = 1
# for i in arr :
#     if n == i :
#         print("founded")
#         counter-=1
#         break
# if counter == 1:
#     print("not found")


#program for finding second max and second min


# default_max = default_min = arr[0]
# for i in range(1,len(arr)):
#     if default_max < arr[i]:
#         default_max = arr[i]
#     elif default_min>arr[i]:
#         default_min = arr[i]

# arr = list(set(arr))
# arr.remove(default_max)
# print("this is second max",max(arr))
# arr.remove(default_min)
# print("this is second min",min(arr))


#program for Binary Search



# arr = [20,21,85,100,600]
# element = int(input())
# low = 0
# high = len(arr)-1

# def BinarySearch(arr,low,high,element):
#     if low<=high:
#         mid = (low+high)//2
#         if element<arr[mid]:
#            return BinarySearch(arr,low,mid-1,element)
#         elif element>arr[mid]:
#            return BinarySearch(arr,mid+1,high,element)
#         else:
#             return mid
#     else:
#         return -1
# result = BinarySearch(arr,low,high,element)
# print(result)
# if result != -1 :
#     print("position of the element is "+str(result))
# else:
#     print("element has not found")



#check if array is sorted

# arr = [1,2,3,4,5,5,5,2]
# counter = 0
# first_element = arr[0]

# for i in range(1,len(arr)):
#     if first_element<=arr[i]:
#         first_element = arr[i]
#         counter+=1
# if counter == len(arr)-1:
#     print("sorted")
# else:
#     print("not sorted")




#merging two arrays

# array_1 = [1,2,3,6]
# array_2 = [7,5,6,8]
# print(array_1+array_2)


#find duplicate in a sorted array

# arr = [3,3,3,2,2,5,6,6]
# duplicates = []
# for i in range(1,len(arr)):
#     if arr[i-1] in arr[i:]:
#         if arr[i-1] not in duplicates:
#             duplicates.append(arr[i-1])
# print(duplicates)


#finding missing elements in a array

#method 1

# arr = [1,2,3,4,4]
# for i in range(len(arr)):
#     if i+1 not in arr :
#         print(i+1)



#reversing an array
 
# arr = [1,3,4,8,7]
# for i in range(len(arr)//2):
#     arr[i],arr[(len(arr)-1)-i] = arr[(len(arr)-1)-i],arr[i]
# print(arr)

