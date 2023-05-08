a, b = list(map(int, input().split()))

hashmap = {}
hashmap[a] = 1


def recurse(n, target):
    if n > target:
        return
    if 2 * n not in hashmap:
        hashmap[2 * n] = hashmap[n] + 1
    else:
        hashmap[2 * n] = min(hashmap[n] + 1, hashmap[2 * n])
    recurse(2 * n, target)

    if int(str(n) + "1") not in hashmap:
        hashmap[int(str(n) + "1")] = hashmap[n] + 1
    else:
        hashmap[int(str(n) + "1")] = min(hashmap[n] + 1, hashmap[int(str(n) + "1")])
    recurse(int(str(n) + "1"), target)


recurse(a, b)

print(hashmap.get(b, -1))
