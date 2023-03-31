my = [list(map(int, input().split())) for i in range(5)]
answer = [list(map(int, input().split())) for i in range(5)]


def check(num):
    for col in range(5):
        for row in range(5):
            if num == my[row][col]:
                my[row][col] = 0
                return


def num_bingo(my):
    bingo = 0
    for i in range(5):
        col_sum = 0
        row_sum = 0
        for j in range(5):
            col_sum += my[j][i]
            row_sum += my[i][j]
        if col_sum == 0:
            bingo += 1
        if row_sum == 0:
            bingo += 1

    diagonal = [0, 1, 2, 3, 4]
    diagonal_sum = 0
    reverse_sum = 0
    for num in diagonal:
        diagonal_sum += my[num][num]
        reverse_sum += my[num][4 - num]

    if diagonal_sum == 0:
        bingo += 1

    if reverse_sum == 0:
        bingo += 1

    return bingo


def main():
    count = 0
    for row in answer:
        for num in row:
            count += 1
            check(num)
            if num_bingo(my) >= 3:
                return count


print(main())
