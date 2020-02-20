# Works for test a, b, c
target = [0, 1, 2]
all_in = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
all_out = ["a.out", "b.out", "c.out", "d.out", "e.out"]
for test in target:
    in_file = open(all_in[test], "r")
    first_line = in_file.readline()
    second_line = in_file.readline()
    in_file.close()
    print(first_line)
    print(second_line)

    m, n = list(map(int, first_line.split(" ")))
    s = list(map(int, second_line.split(" ")))
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(0, m + 1):
            if j >= s[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - s[i - 1]] + s[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    temp = m
    ans = []
    num = 0
    for i in range(n, 0, -1):
        if dp[i][temp] != dp[i - 1][temp]:
            temp -= s[i - 1]
            ans.append(i - 1)
            num += 1
    ans.sort()
    ans_str = []
    for index in ans:
        ans_str.append(str(index))
    ans_final = " ".join(ans_str)

    print(num)
    print(ans_final)
    print(dp[n][m])
    out_file = open(all_out[test], "w")
    out_file.write(str(num) + '\n' + ans_final)
    out_file.close()
