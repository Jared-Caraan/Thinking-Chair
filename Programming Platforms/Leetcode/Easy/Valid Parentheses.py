

def isValid(s: str) -> bool:

    if len(s) <= 1:
        return False
    
    holder =[]
    dict = {
        '(':')',
        '[':']',
        '{':'}'
    }

    for i in s:
        if i in dict:
            holder.append(i)
        else:
            if not holder or dict[holder[-1]] != i:
                return False
            else:
                holder.pop()

    if not holder:
        return True
    
    return False

print(isValid(')))))){'))

# class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
