#Task
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZ BUZZ")
    elif i % 5 == 0:
        print("BUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    else:
        print(i)


#Extra

num1 = input("Choose your first number for FIZZ")
num2 = input("Choose your second Number for BUZZ")
rang = input("choose a range")

for i in range(1, int(rang)):
    if i % int(num1) == 0 and int(num2) % 5 == 0:
        print("FIZZBUZZ")
    elif i % int(num2) == 0:
        print("BUZZ")
    elif i % int(num1) == 0:
        print("FIZZ")
    else:
        print(i)
