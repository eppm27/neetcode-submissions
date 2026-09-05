class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        output = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        pairs = list(count.items())
        pairs.sort(key=lambda x:x[1], reverse=True)

        for i in range(k):
            output.append(pairs[i][0])
        
        return output
        