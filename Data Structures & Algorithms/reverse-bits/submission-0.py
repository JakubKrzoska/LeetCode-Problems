class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            curr_bit = n & (1 << i)
            curr_bit = curr_bit >> i
            res = res | (curr_bit << (31 - i))
        return res