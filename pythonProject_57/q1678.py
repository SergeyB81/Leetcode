class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')


class Solution:
    def interpret(self, command: str) -> str:
        command = list(command)
        n = len(command)

        for i in range(1, n):
            if command[i-1] == '(' and command[i] == ')':
                command[i-1] = 'o'
                command[i] = ''

        for i in range(0,n):
            if command[i] in  ['(', ')']:
                command[i] = ''
# new

        return ''.join(command)



if __name__ == ('__main__'):
    print('sergey')
    command = "G()()()()(al)"
    print(Solution().interpret(command))

    # rep