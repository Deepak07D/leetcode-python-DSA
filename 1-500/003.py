#two pointers-removing duplicates from a sorted array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=1
        a=len(nums)
        for i in range(1,a):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k         
