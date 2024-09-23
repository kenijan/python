

# Logical_Operators

# 1. AND Operator (and)
# Returns True if both statements are true
x = True
y = False
print(f'1. AND Operator (and)   {x} and {y} :', x and y)  # False

# 2. OR Operator (or)
# Returns True if at least one statement is true
x = True
y = False
print(f'2. OR Operator (or)     {x} or {y}  :', x or y)  # True

# 3. NOT Operator (not)
# Reverses the boolean value
x = True
print(f'3. NOT Operator (not)   not {x}       :', not x)  # False

# Combination Example
a = 5
b = 10
c = 15

# Check if 'a' is less than 'b' and 'b' is less than 'c'
print(f'{a} < {b} and {b} < {c}    :', a < b and b < c)  # True

# Check if 'a' is less than 'b' or 'b' is greater than 'c'
print(f'{a} < {b} or {b} > {c}     :', a < b or b > c)  # True

# Using NOT with a condition
print(f'not ({a} > {b})          :', not (a > b))  # True
