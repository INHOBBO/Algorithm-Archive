import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = set(input().rstrip() for _ in range(n))
watch = set(input().rstrip() for _ in range(m))

listen_watch = sorted(list(listen & watch))
print(len(listen_watch))
for name in listen_watch:
    print(name)