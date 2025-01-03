def basic_calculator(num1, num2, operator):
    """ This function takes in two numbers and 
    an operator and returns the result of the operation """
    try:
        # first mode we check the operator
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else:
            return 'Invalid operator'
    # halat dovom ke agar exceptioni pish amad
    except ZeroDivisionError:
        return 'Division by zero is not allowed'
    except TypeError:
        return 'non-numeric input is not allowed'
# test
print(basic_calculator("5",4,'/'))
print(basic_calculator(5,4,'/'))
