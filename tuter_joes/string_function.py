


def partition():
    line = "hello' have a good day "
    print(line)
    print(type(line))
    print(line.upper())
    print(line.lower())
    print(line.capitalize())
    print(line.title())
    print(line.count("h"))
    print(line.find("o"))
    print(line.find("o", 5))  # index  5 ku piraku vara fist 'o'
    print(line.replace("o", "i"))
    print(line.endswith('y'))  # last not 'y'
    print(line.endswith(' '))  # last space so true
#partition()
print("--"*20)

# Function to check different string properties
def check_string_properties(s):
    print(f"String: {s}")
    print(f"Is upper? {s.isupper()}")
    print(f"Is lower? {s.islower()}")
    print(f"Is digit? {s.isdigit()}")
    print(f"Is alphabetic? {s.isalpha()}")
    print(f"Is alphanumeric? {s.isalnum()}")
    print(f"Is space? {s.isspace()}")
    print(f"Is title? {s.istitle()}")
    print(f"Is numeric? {s.isnumeric()}")
    print(f"Is decimal? {s.isdecimal()}")
    print(f"Is identifier? {s.isidentifier()}")
    print(f"Is printable? {s.isprintable()}")
    print(f"Is ASCII? {s.isascii()}")
    print("-" * 30)

# Test strings
test_strings = [
    "HELLO",    # Uppercase
    "hello",    # Lowercase
    "12345",    # Digits
    "hello123", # Alphanumeric
    "     ",    # Spaces
    "Hello"     # Mixed case
]

# Check properties for each test string
#for s in test_strings:
    #check_string_properties(s)

para="     Lorem ipsum dolor sit       amet    "
def para_function():
    print(f'{para}')
    print(f'{len(para)}')

    #strip() removes any whitespace characters from the beginning and the end of the string.
    #lstrip(): Removes leading(left) whitespace.
    print(f'{para.strip()}')
    print(f'{len(para.strip())}')
    # rstrip(): Removes trailing(right) whitespace.
    print(f'{len(para.rstrip())}')

    print(f'{len(para.split())}')
    print(f'{para.split()}')
para_function()
