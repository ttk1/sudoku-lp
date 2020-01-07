import pulp as p


def getValue(i, j, x):
    for v in range(1, 10):
        if p.value(x[i][j][v]) == 1:
            return v
    return None


def myPrint(x):
    print('    0 1 2   3 4 5   6 7 8')
    print('  ┌───────┬───────┬───────┐')
    for i in range(0, 9):
        if i in (3, 6):
            print('  ├───────┼───────┼───────┤')
        print(str(i) + ' │', end='')
        for j in range(0, 9):
            if j in (3, 6):
                print(' │', end='')
            v = getValue(i, j, x)
            if v == None:
                print(' -', end='')
            else:
                print(' ' + str(v), end='')
        print(' │')
    print('  └───────┴───────┴───────┘')


def main():
    prob = p.LpProblem('Sudoku')
    x = p.LpVariable.dicts('x', (range(0, 9), range(0, 9),
                                 range(1, 10)), 0, 1, 'Integer')

    # 各マスに必ず数字が割り当てられるための制約
    for i in range(0, 9):
        for j in range(0, 9):
            prob += p.lpSum([x[i][j][v] for v in range(1, 10)]) == 1

    # 各行に1-9の数字がそれぞれ一回ずつ割り当てられるための制約
    for i in range(0, 9):
        for v in range(1, 10):
            prob += p.lpSum([x[i][j][v] for j in range(0, 9)]) == 1

    # 各列に1-9の数字がそれぞれ一回ずつ割り当てられるための制約
    for j in range(0, 9):
        for v in range(1, 10):
            prob += p.lpSum([x[i][j][v] for i in range(0, 9)]) == 1

    # 各ブロックに1-9の数字がそれぞれ一回ずつ割り当てられるための制約
    for k in range(0, 9):
        for v in range(1, 10):
            prob += p.lpSum([x[k // 3 * 3 + l // 3][k % 3 * 3 + l % 3][v]
                             for l in range(0, 9)]) == 1

    # 盤面の読み込み
    file = open('./problem.txt', 'r', encoding='utf-8')
    for i, line in enumerate(file):
        for j, v in enumerate(line.replace('\n', '').split(' ')):
            if v != '-':
                prob += x[i][j][int(v)] == 1

    prob.solve()
    myPrint(x)


main()
