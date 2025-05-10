class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_ip = ''
        for s in address:
            if s == '.':
                new_ip = new_ip + "[.]"
            else:
                new_ip = new_ip + s
        return new_ip


if __name__ == '__main__':
    ip = "255.100.50.000."
    #print(ip.replace('.','[.]'))
    print('sergey')

    print(Solution().defangIPaddr(ip))

    # rep 2