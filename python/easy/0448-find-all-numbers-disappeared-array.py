class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_list = []
        nums_set = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                new_list.append(i)

        return new_list