arr = [3,2,1]
pointer = len(arr) - 2

x = arr[pointer:]
y = list(x)
y.sort(reverse=True)

arrCheck = list(arr)
arrCheck.sort(reverse=True)
if(arr==arrCheck):
    arr.sort()
    print(arr)
else:
    while(x==y and pointer>0):
        pointer-=1
        x = arr[pointer:]
        y = list(x)
        y.sort(reverse=True)

    y.sort()
    for i in range(len(y)):
        if(y[i]>x[0]):
            x[0] = y[i]
            y.pop(i)
            y.sort()
            x[1:] = y[:]
            break
        else:
            i+=1
    arr[pointer:] = x[:]
    print(arr, pointer)
# if(pointer==0):
  
#  print(x)
# # print(arr[pointer:])


