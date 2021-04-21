#method 1
# string = "AbC"

# for i in range(len(string)):
#     string = list(string)
#     if  ord(string[i])<=90 and ord(string[i])>=65:
#        string[i] = chr(ord(string[i])+32)
#     elif ord(string[i])<=122 and ord(string[i])>=97:
#         string[i] = chr(ord(string[i])-32)
# print(string)   
# print(''.join(string))

# method 2

# string = "Abc"
# user = input("enter in which case you wanna change the string: \n1. UPPERCASE\n2. lowercase\n3. Titlecase")
# string = list(string)
# if user == "1":
#     for i in range(len(string)):
#         if ord(string[i])>=97 and ord(string[i])<=122:
#             string[i] = chr(ord(string[i])-32)
# elif user == "2":
#     for i in range(len(string)):
#         if ord(string[i])<=90 and ord(string[i])>=65 :
#             string[i] = chr(ord(string[i])+32)
# print(''.join(string))

