
#for checking duplicates in a string

#method 1

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


#method 2


# main = "abcaab"
# main+=" "
# index = len(main)-1

# for i in range(1,len(main)):
#     if main[i] == " ":
#         break
#     if main[i-1] in main[i:index]:
#         if main[i-1] not in main[index:]:
#             print(main[i-1],"is duplicate:")
#             main+=main[i-1]