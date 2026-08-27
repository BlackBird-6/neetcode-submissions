class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if c == ")" and opening != "(":
                    return False
                if c == "]" and opening != "[":
                    return False
                if c == "}" and opening != "{":
                    return False
        if stack:
            return False
        return True