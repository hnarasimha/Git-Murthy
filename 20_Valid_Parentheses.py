'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
def isValid(s):
    parentheses_stack = []
    temp_left = ['(','[','{']
    temp_right = [')',']','}']
    for ch in s:
        if ch  in temp_left:
            parentheses_stack.append(ch)
            continue
        if ch in temp_right:
            if len(parentheses_stack) == 0:
                return (False)
            if len(parentheses_stack) > 0:
                if parentheses_stack[-1] == '(' and ch == ')':
                    parentheses_stack.pop()
                    continue
                elif parentheses_stack[-1] == '[' and ch == ']':
                    parentheses_stack.pop()
                    continue
                elif parentheses_stack[-1] == '{' and ch == '}':
                    parentheses_stack.pop() 
                    continue 
                else:
                    return False
                
    if len(parentheses_stack) == 0:
        return(True)
    else:
        return(False)





s = "(])"
print(isValid(s))