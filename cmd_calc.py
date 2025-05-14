print("This is a cmd calculator!")
choice = input("What do you want to do? 1-Sum, 2-Sub, 3-Mul, 4-Div: ")

if choice == '1':
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(f'The sum is {a+b}')
elif choice == '2':
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(f'The sub is {a-b}')
elif choice == '3':
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(f'The multiplication is {a*b}')
elif choice == '4':
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(f'The division is {a/b}')
else:
    print("Invalid choice!")
