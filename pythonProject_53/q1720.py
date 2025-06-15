class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        decoded = [first]
        for i in range(len(encoded)):
            decoded.append(encoded[i] ^ decoded[i])
        return decoded
#encoded[i] = arr[i] XOR arr[i+1], then arr[i+1] = encoded[i] XOR arr[i].

if __name__ == '__main__':
    encoded = [6, 2, 7, 3]
    first = 5
    print(Solution().decode(encoded, first))

# rep 5