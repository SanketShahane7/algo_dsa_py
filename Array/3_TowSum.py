from typing import List



class TowSum:

    #-- Brute Force Approach
    def TowSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i, j]
        return []
    
    #-- Hash Map Approach
    def TowSumHashMap(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}    # ArrayVal -> ArrayIndex
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[nums[i]] = i
        return []


towSum = TowSum()
arr = [2, 7, 11, 15]
target = 9
resultBrute = towSum.TowSumBruteForce(arr, target)
resultHashMap = towSum.TowSumHashMap(arr, target)

print(f"The Output for {arr} with target {target} is {resultBrute}")  # Output: [0, 1]
print(f"The Output for {arr} with target {target} is {resultHashMap}")  # Output: [0, 1]

arr1 = [3, 2, 4, 5, 6, 7]
target1 = 10
resultBrute1 = towSum.TowSumBruteForce(arr1, target1)
resultHashMap1 = towSum.TowSumHashMap(arr1, target1)

print(f"The Output for {arr1} with target {target1} is {resultBrute1}")  # Output: [0, 5]
print(f"The Output for {arr1} with target {target1} is {resultHashMap1}")  # Output: [2, 4]