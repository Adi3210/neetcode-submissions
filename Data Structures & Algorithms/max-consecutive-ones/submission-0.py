class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        consecutiveNumber = 0;
        bestNumber = 0;

        for i, v in enumerate(nums):
            if v == 1:
                consecutiveNumber += 1
                bestNumber = max(bestNumber, consecutiveNumber)
            else:
                consecutiveNumber = 0
    
        return bestNumber
