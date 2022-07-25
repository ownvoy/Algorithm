import sys

input = sys.stdin.readline

numlist = []


def add(x):
    if x not in numlist:
        numlist.append(x)


def remove(x):
    if x in numlist:
        numlist.remove(x)


def check(x):
    if x in numlist:
        print("1")
    else:
        print("0")


def toggle(x):
    if x in numlist:
        numlist.remove(x)
    else:
        numlist.append(x)


def empty():
    global numlist
    numlist = []


def alll():
    empty()
    for i in range(1, 21):
        numlist.append(i)


test_case = int(input().strip())

for _ in range(test_case):
    command = input().strip()
    if command == "all":
        alll()
    elif command == "empty":
        empty()
    else:
        x, y = command.split()
        if x == "check":
            check(int(y))
        elif x == "toggle":
            toggle(int(y))
        elif x == "remove":
            remove(int(y))
        else:
            add(int(y))
