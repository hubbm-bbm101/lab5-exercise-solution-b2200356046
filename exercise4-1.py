number = int(input("Enter N value: "))
oddSum = 0
evenSum = 0
for i in range(1, number+1):
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
print("The sum of the odd numbers is", oddSum)
print("The average of the even numbers is", evenSum/number)
