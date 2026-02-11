class Solution():
    def xorOperation(self, n: int, start: int):
        xor = start
        for i in range(1,n):
            xor = xor ^ (start + 2 * i)
        return xor

if __name__ == '__main__':
    n = 4
    start = 3

    print(Solution().xorOperation(4,3))
