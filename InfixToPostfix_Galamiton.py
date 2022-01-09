#Millborne A. Galamiton BS CPE 2B
OPERATORS = set(['+', '-', '*', '/'])#Initialize the operators
PRIORITY = {'+':1, '-':1, '*':2, '/':2}#Initialize the operators with their value
def infix_to_postfix(formula):#Process were the entered infix expression is being converted
    stack = [] 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        else:
            while stack and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack: 
        output += stack.pop()
    
    return output#return the output after being converted

print("INFIX TO POSTFIX CONVERTER")#ask the user to input an Infix expression
expr = input("Enter a infix Expression: ")
print(infix_to_postfix(expr))#pass the entered expression above to convert
