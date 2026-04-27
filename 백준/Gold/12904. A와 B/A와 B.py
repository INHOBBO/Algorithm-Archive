import sys
sys.setrecursionlimit(10**6) # 재귀 호출 리밋 올리기
S=list(input())
T=list(input())
def dfs(t):
    if t==S:
        print(1)
        sys.exit()
    if len(t)==0:
        return
    if t[-1]=='A': # 마지막이 A이면
        dfs(t[:-1]) # 제거하고, 재귀
    if t[-1]=='B': # 마지막이 B이면
        dfs(t[:-1][::-1]) # 제거하고, 뒤집어서 재귀
dfs(T)
print(0)