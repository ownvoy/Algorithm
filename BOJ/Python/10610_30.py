n = int(input())


def thirthy(n):
    if "0" not in str(n):
        print(-1)
        return
    else:
        temp = list(str(n))
        temp.remove("0")
        n = "".join(temp)

    ssum = sum(map(int, list(str(n))))
    if ssum % 3 == 0:
        print("".join(sorted(str(n), reverse=True)) + "0")
        return
    else:
        print(-1)
        return


thirthy(n)