a = int(input("Please enter number a: "))
b = int(input("Please enter number b: "))

answer = 0
while a <= b:
    if a % 2 == 1:
        answer += a
    a += 1

print(answer)
