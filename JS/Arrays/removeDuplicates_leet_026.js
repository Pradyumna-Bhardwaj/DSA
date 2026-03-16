nums = [1,1,2]

const removeDuplicates =(nums) => {

    write = 1;

    for (let read =1; read<nums.length; read++){
        if(nums[read-1]!=nums[read]){
            nums[write] = nums[read];
            write++;
        }
    }
    return write;
}

console.log(removeDuplicates(nums))