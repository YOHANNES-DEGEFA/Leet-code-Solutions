class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, char in enumerate(order):
            d[char] = i 

        for i, word in enumerate(words[:-1]):
            l = 0 
            next_word = words[i+1]
            n, m = len(word), len(next_word)
            k = min(n,m)
            while l < k: 
                if d[word[l]] < d[next_word[l]]:
                    break
                elif d[word[l]] > d[next_word[l]]:
                    return False

                else: # if both are equal 
                    while l < k and d[word[l]] == d[next_word[l]]:
                        if d[word[l]] < d[next_word[l]]:
                            break
                        if d[word[l]] > d[next_word[l]]:
                            return False
                        l += 1 

                    if l == k:
                        if k < n: 
                            return False
                        



        return True