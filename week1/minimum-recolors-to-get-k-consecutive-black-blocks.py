class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolor, cur_recolor = float('inf'), 0 

        l = 0 
        for r in range(len(blocks)):
            cur_recolor += blocks[r] == 'W'
            if r-l+1 == k: 
                min_recolor = min(cur_recolor,min_recolor)
                cur_recolor -= blocks[l] == 'W'
                l += 1 
        return min_recolor

        