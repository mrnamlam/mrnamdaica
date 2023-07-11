x = int(input("Please enter x value: "))
y = int(input("Please enter y value: "))
z = int(input("Please enter z value: "))

if x % 2 == 0:
    if y >= 20:
        print("y is greater than or equal to 20.")
    else:
        print("y is less than 20.")
else:
    if z >= 30:
        print("z is greater than or equal to 30.")
    else:
        print("z is less than 30.")

a = int(input("Please enter number a: "))
b = int(input("Please enter number b: "))
c = int(input("Please enter number c: "))

average = (a + b + c)/3

print(average)