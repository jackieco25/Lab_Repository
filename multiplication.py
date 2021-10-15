name = input("What is your name?")
number = int(input("Enter a number: "))
multiplication = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(name,", here are the multiples of ", number)
for x in multiplication:
    product = number * x
    print(number,"*",x,"=",product)
