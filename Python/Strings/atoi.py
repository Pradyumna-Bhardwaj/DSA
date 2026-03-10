s = "-+12"
output = " "
for i in s:
    if(i == "+" or i == "-" and (output[-1].isdigit() or output[-1] == "-" or output[-1] == "+")):
        break
    if(i=="+" or i=="-" or i.isdigit()):
        output = output + i
    if(not(i.isdigit()) and output[-1].isdigit()):
        break
    if(not(i.isdigit()) and i != " " and output[-1] == " "):
        break
if(output == " " or output[-1] == "-" or output[-1] == "+"):
    output = 0
    print(output)
output = int(output[1:])
if(output < pow(-2,31)):
    output = pow(-2,31)
elif(output > pow(2,31)):
    output = pow(2,31)
print(output)
    
    