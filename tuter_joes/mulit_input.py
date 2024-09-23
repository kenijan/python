# mulit_input
name1,name2,name3 = input("enter the name 3 : ").split(',')
print(name1)
print(name2)
print(name3)

print("*"*30)

# mulit_input
item = []
print('enter tha para')
while True:
    para = input()
    if para:
        item.append(para)
    else:
        break
print('\n'.join(item))

