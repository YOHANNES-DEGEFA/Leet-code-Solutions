class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        seen, N = set(), len(cards)
        l, minNum = 0, N + 1
        for r in range(N):
            while cards[r] in seen: 
                minNum = min(r-l+1,minNum)
                seen.remove(cards[l])
                l += 1 
            seen.add(cards[r])

        return minNum  if minNum < N+1 else -1 
        