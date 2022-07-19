class Solution:
    def isValid(s: str) -> bool:
        stack = [-1]
        for i in s:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)

        return True if len(stack) == 1 else False
