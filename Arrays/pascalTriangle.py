n = int(input("Enter n: "))
finalList = []

finalList.append([1])

if (n>=2):
    finalList.append([1,1])

for currRowNo in range(3,n+1):
    i=1
    row = [0]*(currRowNo)
    row[0]=1
    while(i<int(currRowNo-1)):
        row[i] = finalList[currRowNo-2][i-1] + finalList[currRowNo-2][i]
        i+=1
    row[currRowNo-1] = 1
    finalList.append(row)
print(finalList)


        
    