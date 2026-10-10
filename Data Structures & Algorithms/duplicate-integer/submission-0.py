class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lis = []
        for i in nums :
            if i in lis:
                return True
            else :
                lis.append(i)
        else:
            return False 
