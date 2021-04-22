#method 1

# main = "abbc"
# to_compared = "abcc"
# counter = 0
# for i in main:
#     if i in to_compared:
#         counter+=1
# if len(main) == len(to_compared) == counter:
#     print("anagram")
# else:
#     print("nope")



#method 2

# main = "abbc"
# to_compared = "abcc"
# for i in range(len(main)):
#     if main[i] in to_compared:
#         if i == len(main)-1 and len(main) == len(to_compared):
#             print("anagram string")
#     else:
#         print("Not a anagram string")