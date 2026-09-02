class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        for char in t:
            if char in countt:
                countt[char] += 1
            else:
                countt[char] = 1
        if counts == countt:
            return True
        return False