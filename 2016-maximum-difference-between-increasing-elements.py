from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = nums[0]
        diference = -1

        for num in nums: 
           if(num < min_value):
              min_value = num
        
           diference = max(diference, num - min_value)   

        if(diference == 0):
           return -1  

        return diference
    

print(Solution.maximumDifference(self= None, nums=[7,1,5,4] )  ) 