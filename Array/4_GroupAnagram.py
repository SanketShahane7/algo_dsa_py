# from collections import defaultdict
from typing import List, DefaultDict


class GroupAnagram:
    
    #-- Using Sort technique | the time complexity: O(N * K log K) and space complexity: O(N * K)
    def groupAnagramSort(self, strs: List[str]) -> List[List[str]]:
        res = DefaultDict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        
        return list(res.values())
    
    #-- Using HashMap technique | the time complexity: O(N * K) and space complexity: O(N * K)
    def groupAnagramHashMap(self, strs: List[str]) -> List[List[str]]:
        res = DefaultDict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)
        
        return list(res.values())


# intialise the List[str] with sample values
strList: List[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]

grpAna = GroupAnagram()

groupAnagramSort: List[List[str]] = grpAna.groupAnagramSort(strList)
print(f"-- Output of group anagram sort: {groupAnagramSort}")

groupAnagramHashMap: List[List[str]] = grpAna.groupAnagramHashMap(strList)
print(f"-- Output of grout anagram HashMap: {groupAnagramHashMap}")


