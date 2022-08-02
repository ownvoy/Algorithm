import sys

input = sys.stdin.readline

n = int(input().strip())

numlist = list(map(int, input().strip().split()))

matrix = [[] for _ in range(n + 1)]
for idx, num in enumerate(numlist):
    if num == -1:
        continue
    matrix[num].append(idx)
count = 0
delete_num = int(input().strip())

stack = []

root = numlist.index(-1)


def dfs(start, delete):
    global count
    if delete == root:
        return
    else:
        stack.append(root)
        while stack:
            node = stack.pop()
            info = len(matrix[node])
            if info == 0:
                count += 1
            for h in matrix[node]:
                if h == delete:
                    if info == 1:
                        count += 1
                    continue
                stack.append(h)


dfs(0, delete_num)

print("%d" % count)
