class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, s in enumerate(stones):
            stones[i] = -s

        heapify(stones) # time complexity is O(N)

        while stones:
            s1 = -heappop(stones) # O(Logn)
            if not stones:
                return s1
            s2 = -heappop(stones)
            if s1>s2:
                heappush(stones,s2-s1)

        return 0
