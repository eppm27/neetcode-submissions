class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countt = {}
        counts = {}
        for char in t:
            if char in countt:
                countt[char] += 1
            else:
                countt[char] = 1
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        return countt == counts