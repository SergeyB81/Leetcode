class Solution:
    def intercept(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')

class Solution1:
    def intercept(self, command: str) -> str:
        n = len(command)
        command = list(command)

        for i in range(1, n):
            if command[i-1] == '(' and command[i] == ')':
                command[i-1] = 'o'
                command[i] = ''

        for i in range(0, n):
            if command[i] in ['(', ')']:
                command[i] = ''

        return ''.join(command)




if __name__ == '__main__':
    print('ok')
    command = "G()()()()(al)"
    print(Solution().intercept(command))
    print(Solution1().intercept(command))