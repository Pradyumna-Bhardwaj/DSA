x = -123
if(x<0):
    y = str(x)[1:]
else:
    y = str(x)

reversed = ""
for i in range(len(y)):
    reversed = reversed + (y[len(y)-1-i])

if(x<0):
    reversed = "-" + reversed
    
if(int(reversed)>=pow(-2, 31) and int(reversed)<=pow(2,31)):
    print(int(reversed))
else:
    print(0)
    