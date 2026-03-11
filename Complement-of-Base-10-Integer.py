1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        if n == 0:
4            return 1  # Edge case: complement of 0 is 1
5        # Create a mask with all 1s of the same length as n in binary
6        mask = (1 << n.bit_length()) - 1
7        # XOR n with mask to get the complement
8        return n ^ mask