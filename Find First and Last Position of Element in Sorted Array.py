class Solution(object):
        
    def leftMost(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while(low <= high):
            mid = (low + high) / 2
            if(nums[mid] == target):
                if(mid ==low or nums[mid-1] != target):
                    return mid
                high = mid -1
            elif(nums[mid] > target):
                high = mid -1
            else:
                low = mid + 1
        return -1
     
    def rightMost(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while(low <= high):
            mid = (low + high) / 2
            if(nums[mid] == target):
                if(mid == high or nums[mid+1] != target):
                    return mid
                low = mid + 1
            elif(nums[mid] > target):
                high = mid -1
            else:
                low = mid + 1
        return -1
    
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.leftMost(nums, target)
        right = self.rightMost(nums, target)
        return [left, right]
