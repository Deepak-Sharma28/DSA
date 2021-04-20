k = int(input())

arr= [1,3,1,5]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == k:
            print([i,j])



