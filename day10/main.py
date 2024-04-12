from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  
  operations = {
    "+": add,
    "-": subtract, 
    "*": multiply, 
    "/": divide
  }
  
  for operation in operations:
    print(operation)
  
  end_calc = False
  
  while not end_calc:  
    operation_symbol = input("Pick an operation: ")
    
    num2 = float(input("What's the next number?: "))
    
    result = operations[operation_symbol](num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {result}")
    
    continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.: ").lower()
    if continue_calc == "y":
      num1 = result
    else:
      end_calc = True
      calculator()

calculator()


