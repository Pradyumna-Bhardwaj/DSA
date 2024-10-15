n = int(input("Enter n: "))
finalList = []
finalList.append([1])
finalList.append([1,1])
if (n==1):
    print(finalList[0])
elif(n==2):
    print(finalList)
for currRowNo in range(3,n+1):
    i=1
    row = [0]*(currRowNo)
    row[0]=1
    while(i<int(currRowNo-1)):
        row[i] = finalList[currRowNo-2][i-1] + finalList[currRowNo-2][i]
        i+=1
    row[currRowNo-1] = 1
    # if(n%2!=0):
    finalList.append(row)
#now copy the first of list to 2nd half


print(finalList)


        
    