//https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=my9teg7v

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function(nums, target) {
  const hashmap ={}

  for(let i = 0; i < nums.length; i++){
    const  requiredNum = target - nums[i]
    if(hashmap[requiredNum] > -1){
      return [hashmap[requiredNum], i]
    }
   
    hashmap[nums[i]] = i;
  }
  
  return [];
};
