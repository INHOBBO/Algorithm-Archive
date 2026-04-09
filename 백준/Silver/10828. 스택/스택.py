import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    command_type = command[0]

    if command_type == 'push':
        stack.append(command[1])
    elif command_type == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command_type == 'size':
        print(len(stack))
    elif command_type == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command_type == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])