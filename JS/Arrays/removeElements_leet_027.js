let nums = [0,1,2,2,3,0,4,2]
// let val = 2

const removeElements = (nums, val) => {
    let val_pointer = 0
    // let temp = 0
    for (let i=0; i<nums.length; i++){
        if(nums[i] != val){
            // temp = nums[i]
            // nums[i] = nums[val_pointer] 
            nums[val_pointer] = nums[i] 
            val_pointer ++   
        }
    }
    console.log(nums)
    return val_pointer
}

console.log(removeElements(nums,2))