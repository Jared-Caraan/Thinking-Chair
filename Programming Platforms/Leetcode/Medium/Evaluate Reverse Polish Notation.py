# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
def evalRPN(tokens):
    operand = []
    operators = '+-*/'
    ans = int(tokens[0])

    for i in tokens:
        if i not in operators:
            operand.append(i)
            continue
        if i in operators:
            op_2 = operand.pop()
            op_1 = operand.pop()
            ans = int(eval(str(op_1) + i + str(op_2)))
            operand.append(ans)
        
    return ans

print(evalRPN(["18"]))