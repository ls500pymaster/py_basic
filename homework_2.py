number = int(input("Input 4 digit number: "))
left, right = divmod(number, 1000)
print(left)
left, right = divmod(right, 100)
print(left)
left, right = divmod(right, 10)
print(left)
left, right = divmod(right, 1)
print(left)