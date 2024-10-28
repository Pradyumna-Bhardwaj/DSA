digits = [9]

number = 0
for i in range(len(digits)):
    number = number + (digits[len(digits) - 1 - i] * (pow(10, i)))
number += 1
res = [int(x) for x in str(number)]
print(res)