number = int(input("Input 4 digit number: "))
first, right_side = divmod(number, 10000)
print(first)
second, right_side = divmod(number, 1000)
print(second)
third, right_side = divmod(number, 100)
fourth, right_side = divmod(number, 10)
fifth, right_side = divmod(number, 1)