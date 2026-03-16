s = ["o"]

const reverseString = (s) =>{
    let end = s.length -1
    let start = 0
    let temp

    while(start<end){
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start++;
        end --;
    }
    return s
}

console.log(reverseString(s))