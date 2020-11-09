#question 4.a #
def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

#def print_arguments(func):

def print_arguments(*args):
    print(f'Arguments are: {args}')


augmented_multiply_by_two = print_arguments(multiply_by_two(10))
x = augmented_multiply_by_two

augmented_add_numbers = print_arguments(add_numbers(3, 4))
x = augmented_add_numbers

#question 4.b #
def add_numbers(a, b):
    return a+b

def multiply_output(addnum):
    return 2*addnum
# def multiply_outputs(func):

def print_arguments(args):
    print (f'Arguments are:{args}')
    
augmented_add_number = (add_numbers(3,4))
x=augmented_add_number

augmented_output=print_arguments(multiply_output(x))
ambt=augmented_output

#question 4.c #
def multiply_by_three(x):
    return x*3

def multiply_output(ambt):
    return 2*ambt

#print_arguments(args, **kwargs):

def print_arguments(args):
    print (f'Arguments are:{args}')
    
augmented_multiply_by_three = (multiply_by_three(10))
x=augmented_multiply_by_three
augmented_output=print_arguments(multiply_output(x))
ambt=augmented_output
