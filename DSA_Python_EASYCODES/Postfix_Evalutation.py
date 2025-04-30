from Stack_Implementation import Stack

def postfix_eval(expression):
    stack = Stack()
    
    for i in expression.split():
        if i.isdigit():
            stack.push(int(i))
        else:
            b= stack.pop()
            a= stack.pop()
            
            if i == '+':
                stack.push(a + b)
            elif i == '-':
                stack.push(a - b)
            elif i == '*':
                stack.push(a * b)
            elif i == '/':
                stack.push(a / b)
    return stack.pop()

if __name__ == "__main__":
    expression = "3 4 + 2 * 7 /"
    result = postfix_eval(expression)
    print(f"Result of postfix expression '{expression}' is: {result}")  # Output: 2.0
