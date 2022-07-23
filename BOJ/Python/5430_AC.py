import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input().strip())


def test():
    for _ in range(testcase):
        funclist = list(input().strip())
        number = int(input().strip())
        numlist = input().strip().replace(",", "*").replace("[", "*").replace("]", "*")
        numlist = numlist.split("*")
        numlist.remove("")
        numlist.remove("")
        if number == 0:
            numlist.remove("")
        numlist = deque(map(int, numlist))
        error = 0
        R_count = 0
        for func in funclist:
            if func == "R":
                R_count += 1
            if func == "D":
                if numlist:
                    if R_count % 2 == 0:
                        numlist.popleft()
                    else:
                        numlist.pop()
                else:
                    error = 1
                    break
        if R_count % 2 == 1:
            numlist.reverse()
        if error == 1:
            print("error")
        else:
            print("[" + ",".join(map(str, numlist)) + "]")


test()
