
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