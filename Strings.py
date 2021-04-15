#checking if a string is a anagram or not

#method 1

# main = "abc"
# to_compared = "bca"
# counter = 0
# for i in main:
#     if i in to_compared:
#         counter+=1
# if len(main) == len(to_compared) == counter:
#     print("anagram")
# else:
#     print("nope")


#method 2

# main = "abc"
# to_compared = "baa"
# for i in range(len(main)):
#     if main[i] in to_compared:
#         if i == len(main)-1 and len(main) == len(to_compared):
#             print("anagram string")
#     else:
#         print("Not a anagram string")


#for reversing a string

# user = "abcd"
# for i in range(len(user)//2):
#     user = list(user)
#     user[i],user[(len(user)-1)-i] = user[(len(user)-1)-i],user[i]
# print(*user)


#program for checking palidrome sting


# String = "aba"
# temp = ""
# for i in range(-1,-len(String)-1,-1):
#     temp+=String[i]
# if String == temp:
#     print("Palindrome")
# else:
#     print("Nope")


#for checking duplicates in a string

# main = "abcdadc"
# temp = ""
# for i in range(1,len(main)):
#     if main[i-1] in main[i:]:
#         if main[i-1] not in temp:
#             temp+=main[i-1]
# if len(temp)!= 0:
#     print(temp)
# else:
#     print("no duplicates")
