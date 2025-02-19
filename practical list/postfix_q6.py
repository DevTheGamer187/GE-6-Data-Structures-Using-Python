from stack_q4 import Stack
def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token.isdigit():  
            stack.push(int(token)) 
        elif token in operators:  
            b = stack.pop()  
            a = stack.pop() 

            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)  
    return stack.pop()  

# Example usage
postfix_expr = "5 3 + 8 2 - *"  
result = evaluate_postfix(postfix_expr)
print("Result:", result) 