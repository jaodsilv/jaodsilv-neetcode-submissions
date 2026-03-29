class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)
        #print(n, b)
        b = b[:2] + (b[2:][::-1]) + ('0' * (34-len(b)))
        #print(b, int(b, 2))
        return int(b, 2)