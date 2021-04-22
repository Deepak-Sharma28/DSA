def postfix_conversion(s):
    stack = []
    operators = {
        '+':1,
        '-':1,
        '*':2,
        "/":2,
        '^':3,
        "(":0
    }

    postfix = " "

    for i in range(len(s)):
        if (s[i].isalpha()) == True:
            postfix+=s[i]
        elif s[i] == "(":
            stack.append(s[i])
        elif s[i] in ["+","-","/","*","^"]:
            if len(stack) == 0:
                stack.append(s[i])
            else:
                while len(stack)!=0 and operators[s[i]]<=operators[stack[-1]]:
                    postfix+=stack.pop()
                stack.append(s[i])
        elif s[i] == ")":
            while stack[-1] != "(":
                postfix+=stack.pop()
            stack.pop()
    while len(stack) > 0:
        postfix+=stack.pop()
    return postfix
s= "A*(B+C/D)"
print(postfix_conversion(s))

