# Nested_For_Loop

for i in range(5):
    for j in range(i):
        print('*',end='')
    print('')
print("-"*30)

for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"Outer loop i = {i}, Inner loop j = {j}")
print("-"*30)

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()  # For new line after each row

