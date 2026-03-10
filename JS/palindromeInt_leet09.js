x = 124521
xLength = x.toString().length
xString = x.toString()

for (let i=0; i< xLength/2; i++) {
    if(xString[i] == xString[xLength-i-1]){
        continue
    }
    else{
        console.log("x is not a palindrome")
        break;
    }
}

