arr = [3,5,2,1]
for i in range(len(arr)-1):
    min_num = i
    for j in range(i+1,len(arr)):
        if arr[min_num]>arr[j]:
            min_num = j
    if arr[min_num] != arr[i]:
        arr[i],arr[min_num] = arr[min_num],arr[i]
print(arr)