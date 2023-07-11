a = input("Please, enter your name: ")
print('K' in a)

b = input("Enter the first word: ")
c = input("Enter the second words: ")
print(b is c)

age = int(input("Plese enter your dog's age: "))
if age < 5:
    print("Your dog is very young.")
else :
    print("Your dog is gonna die very soon.")

score = float(input("Please, enter your score: "))

if score >= 90: 
    print("You passed A+")
elif score >= 80:
    print("You passed A")
elif score >= 70:
    print("You passed B+")
elif score >= 60:
    print("You passed B")
elif score >=50:
    print("You passed C")
else:
    print("You failed, bitches!")

