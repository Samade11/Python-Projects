#CALCULATOR
from Calculator_Art import logo
print(logo)

#ADD
def add(n1, n2):
    """will add together two given numbers(ints)"""
    return n1 + n2

#SUBTRACT
def subtract(n1, n2):
    """will subtract two given numbers(ints)"""
    return n1 - n2

#DIVIDE
def divide(n1, n2 ):
    """will divide two given numbers(ints)"""
    return n1 / n2

#MULTIPLY
def multiply(n1, n2):
    """will multiple two given numbers(ints)"""
    return n1 * n2

operator_dic = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
}

#function uses dictionary to perform operation that has been called on given numbs
function = operator_dic["*"]
function(2,3)

def calculator():
    """Calculator that performs multiple operations that user can chose from """
    numb1 = float(input("What is the first number? "))

    for symbol in operator_dic:
        print(symbol)
    more_calc = True

    while more_calc:
        op_symbol = input("Which operator would you like to use?: ")
        numb2 = float(input("What is the next number? "))
        #used to make calculations
        calc_func = operator_dic[op_symbol]
        answer = calc_func(numb1, numb2)

        print(f"{numb1} {op_symbol} {numb2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ") == "y":
            numb1 = answer
        else:
            more_calc = False
            #condition must be met for the calculator function to be able to call itself 
            calculator()

calculator()