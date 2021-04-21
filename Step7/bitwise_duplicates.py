string = "aabc"
string+= " "
index = len(string)-1
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if (~ord(string[j])) == ~ord(string[i]):
            if string[i] not in string[index:]:
                string+=string[i]
                print(string[i],end="")
