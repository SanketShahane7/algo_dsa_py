class Anagram:
    def isAnagramUsingSorting(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
    def isAnagramUsingHashMap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
anagram = Anagram()
s1 = "listen"
s2 = "silent"

# result = anagram.isAnagramUsingSorting(s1, s2)
result = anagram.isAnagramUsingHashMap(s1, s2)


print(f"The Output for '{s1}' and '{s2}' is {result}")  # Output: True