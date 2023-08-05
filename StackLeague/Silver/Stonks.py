def trader(stock_prices):
    counter = 0
    stack = []

    for i in stock_prices:
        if stack and i < stack[-1]:
            stack = []
        stack.append(i)
        counter = max(len(stack), counter)
    
    return 1 if counter <= 1 else counter

print(trader([0,1,1,0,4,5,6]))