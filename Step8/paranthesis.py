# def isBalaced(s):
#     stack = []
#     for i in s:
#         if i in "(,[,{":
#             stack.append(i)
#         else:
#             if len(stack) == 0:
#                 return False
#             else:
#                 if i == ')' and '(' in stack:
#                     stack.pop()
#                 elif i == ']' and '[' in stack:
#                     stack.pop()
#                 elif i == '}' and '{' in stack:
#                     stack.pop()
#     if len(stack) == 0:
#         return True
#     else:
#         return False

# brackets = input()

# print(isBalaced(brackets))