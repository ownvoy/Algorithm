from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    testcase = list(map(int, input().strip().split()))
    priority = deque(list(map(int, input().strip().split())))
    target = testcase[1]
    count = 0
    while (1):
        a = priority.popleft()
        priority.appendleft(a)
        
        if(a == max(priority)):
            if( target == 0 ):
                count +=1
                print(count)
                break
            else:
                priority.popleft()
                target-=1
                count +=1
        else:
                priority.popleft()
                priority.append(a)
                if(target ==0):
                    target = len(priority) - 1
                else:
                    target -= 1
