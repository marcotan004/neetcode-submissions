class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        keys = [[] for i in range(len(nums))]
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key in count:
            keys[count[key] - 1].append(key)

        ret = []
        n_ret = 0
        for i in range(len(nums) - 1, -1, -1):
            while keys[i]:
                ret.append(keys[i].pop())
                n_ret += 1
                
                if n_ret == k:
                    return ret
        
        return ret