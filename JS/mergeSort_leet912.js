nums = [5,1,1,2,0,0]


function merge(left,right){

    let result = [];
    let i = 0;
    let j = 0;

    while(i<left.length && j<right.length){
        if(left[i]<right[j]){
            result.push(left[i]);
            i++;
        }
        else{
            result.push(right[j]);
            j++;
        }
    }
    return result.concat(left.slice(i)).concat(right.slice(j));
}




function mergeSort(nums){
    if (nums.length <=1) return nums;

    //divide array
    let mid = Math.floor(nums.length/2);
    let left = mergeSort(nums.slice(0, mid));
    let right = mergeSort(nums.slice(mid));

    //merge array
    let sorted = merge(left, right);
    return sorted; 
}


let sorted = mergeSort(nums);
console.log(sorted)