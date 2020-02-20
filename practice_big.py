# Works for test d, e
# Suggested time for test d(target = 3) is 2000, best solution when showing 9833203
# Suggested time for test e(target = 4) is 200, best solution when showing 248968438

from random import randint

target = [3, 4]
time = [2000, 200]
for k in range(2):
    all_in = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
    all_out = ["a.out", "b.out", "c.out", "d.out", "e.out"]
    in_file = open(all_in[target[k]], "r")
    first_line = in_file.readline()
    second_line = in_file.readline()
    in_file.close()

    m, n = list(map(int, first_line.split(" ")))
    s = list(map(int, second_line.split(" ")))
    m = sum(s) - m
    max_s = max(s)
    max_ans_sum = 0
    max_ans_num = 0
    max_ans = []
    num_map = [-1 for _ in range(max_s + 1)]
    for i in range(n):
        if num_map[s[i]] == -1:
            num_map[s[i]] = i

    for i in range(time[k]):
        ans = []
        temp = s[:]
        ans_num = 0
        max_index = n - 1
        remain = m

        while remain >= temp[0]:
            while temp[max_index] > remain:
                max_index -= 1
            pick = randint(0, max_index)
            remain -= temp[pick]
            ans.append(num_map[temp[pick]])
            ans_num += 1
            temp.pop(pick)
            max_index -= 1

        ans_sum = m - remain
        if ans_sum > max_ans_sum:
            max_ans_sum = ans_sum
            max_ans_num = ans_num
            max_ans = ans[:]

    max_ans.sort()
    for i in range(1, len(max_ans)):
        if s[max_ans[i]] == s[max_ans[i - 1]]:
            max_ans[i] = max_ans[i - 1] + 1
    ans_str = []
    for i in range(n):
        if i not in max_ans:
            ans_str.append(str(i))
    ans_final = " ".join(ans_str)
    num = n - max_ans_num

    print(max_ans_sum)
    print(num)
    print(ans_final)

    out_file = open(all_out[target[k]], "w")
    out_file.write(str(num) + '\n' + ans_final)
    out_file.close()
