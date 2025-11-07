class Duplicate:
    @staticmethod
    def hasDuplicateBruteForce(nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    def hasDuplicateSort(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
    def hasDuplicateUsingHashSet(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


duplicate = Duplicate()
arr = [1, 2, 3, 4, 3]

# result = duplicate.hasDuplicateBruteForce(arr)
# result = duplicate.hasDuplicateUsingHashSet(arr)
result = duplicate.hasDuplicateSort(arr)


print(f"The Output for {arr} is {result}")  # Output: True


