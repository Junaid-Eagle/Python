# variable : object containing data
a = 10
b = 20
c = a + b
sum = "the sum of a and b"
print(c) # Output: 30
# types of variable
print(type(a))
print(type(sum))

# Rules to assign a variable    
# 1. Variable name should not start with a number
# 2. Variable name should not contain any special character except underscore(_).       
# 3. Variable name should not be a keyword
variable_name = "John Doe"   # valid variable name
# 1number = 10                    # invalid variable name, starts with a digit
# $dollar = 100                   # invalid variable name, contains dollar sign ($)
# sp@cial = 100                   # invalid variable name, contains @ symbol
# """invalid variable name, contains multiple lines"""
# \nnewline=100                # invalid variable name, contains newline character (\n)   
# '''invalid variable name, contains single quote(')'''
# 'singlequote' = 100            # valid variable name, contains single quote(') but it is inside triple quotes("")
# 'singlequote' = 100             # valid variable name, contains single quote(') but it is inside triple quotes("")
# 'singlequote' = 100             # valid variable name, contains single quote(') but it is inside triple quotes("")