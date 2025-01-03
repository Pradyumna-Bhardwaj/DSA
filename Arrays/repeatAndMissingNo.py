A = [3,1,2,5,3]
n = len(A)
sumArr = sum(A)
sumLen = n*(n+1)/2
diffNos = sumLen - sumArr
sumSquaresArr = sum(map(lambda i: i * i, A))
sumSquaresLen = (n * (n + 1) * (2 * n + 1)) // 6
diffSquares = sumSquaresLen - sumSquaresArr
sumNos = diffSquares/diffNos
result = [int((sumNos-diffNos)/2),int((diffNos + sumNos)/2)]

print("[repeated no., missing no.] = ",result)
