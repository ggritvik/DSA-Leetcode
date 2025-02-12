s = "({[]})"
stack = []

def ValidParentheses(s):
    if len(s) == 0:
        print("False")
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        else:
            if stack:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    print("False")
            else:
                print("False")
                
    if len(stack) == 0:
        print("True")
    else:
        print("False")

ValidParentheses(s)