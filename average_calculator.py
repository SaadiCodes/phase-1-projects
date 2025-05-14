print("This calculator calculates the average of all the numbers you enter.")
n = 0
t = 0
while True:
    a = int(input("Enter the number: "))
    t += a
    n += 1
    choice = int(input("Do you want to continue? 0 FOR NO, 1 FOR YES "))
    if choice == 1:
        continue
    elif choice == 0:
        break
average = t/n
print(int(average))