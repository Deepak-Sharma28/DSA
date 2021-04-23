arr = []
def permutation(i,string,arr):
    if i == len(string):
        arr.append(string)
    else:
        k = []
        for s in string:
            k.append(s)
        for j in range(i,len(string)):
            k[i],k[j] = k[j],k[i]
            string = ''.join(k)
            permutation(i+1,string,arr)
            k[i],k[j] = k[j],k[i]
        return arr
string = input()
print(permutation(0,string,arr))
    