nums = [-1,0,3,5,9,12]

function binarySearch(nums, target){
    left = 0;
    right = nums.length - 1;

    while(left <= right){
        mid = Math.floor((left+right)/2);

        console.log("left = ", nums[left]);
        console.log("right = ", nums[right]);
        console.log("nums[mid] = ", nums[mid]);

        if(nums[mid]==target){
            return mid;
        } 

        target < nums[mid] ? right = mid - 1 : left = mid + 1;
    }
    return ("target not found");
}

output = binarySearch(nums, 9)
console.log(output)