import math


def solution(brown, yellow):
    answer = []
    yellow_root = math.floor(math.sqrt(yellow))
    decomposition = {}

    for i in range(1, yellow_root + 1):
        if yellow % i == 0:
            decomposition[i] = yellow // i

    decomposition = list(decomposition.items())

    for numbers in decomposition:
        each_brown = numbers[0] * 2 + numbers[1] * 2 + 4
        if each_brown == brown:
            row = numbers[0] + 2
            col = numbers[1] + 2
            answer = [col, row]
            return answer


print(solution(8, 1))

# brown, yellow = map(int, input().strip().split())

# decomposition = {}
# for i in range(1, yellow_root + 1):
#     if yellow % i == 0:
#         decomposition[i] = yellow // i

# decomposition = list(decomposition.items())

# for numbers in decomposition:
#     each_brown = numbers[0] * 2 + numbers[1] * 2 + 4
#     if each_brown == brown:
#         row = numbers[0] + 2
#         col = numbers[1] + 2
#         print([col, row])
