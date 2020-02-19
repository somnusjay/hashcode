# Works for test d, e
# Suggested time for test d(target = 3) is 2000, best solution when showing 9833203
# Suggested time for test e(target = 4) is 200, best solution when showing 248968438

from random import randint

target = 4
time = 200
all_in = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
all_out = ["a.out", "b.out", "c.out", "d.out", "e.out"]
in_file = open(all_in[target], "r")
first_line = in_file.readline()
second_line = in_file.readline()
in_file.close()

m, n = list(map(int, first_line.split(" ")))
s = list(map(int, second_line.split(" ")))
m = sum(s) - m
max_ans_sum = 0
max_ans_num = 0
max_ans = []
num_map = {}
for i in range(len(s)):
    num_map[s[i]] = i

for i in range(time):
    ans = []
    temp = s[:]
    ans_num = 0
    min_index = 0
    max_index = n - 1
    remain = m

    while remain >= temp[min_index]:
        left = min_index
        right = max_index
        while left < right:
            mid = int((left + right) / 2)
            if temp[mid] > remain:
                right = mid
            else:
                left = mid + 1
        max_index = left
        pick = randint(min_index, max_index - 1)
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
ans_str = []
for i in range(n):
    if i not in max_ans:
        ans_str.append(str(i))
ans_final = " ".join(ans_str)
num = n - max_ans_num

print(max_ans_sum)
print(num)
print(ans_final)

out_file = open(all_out[target], "w")
out_file.write(str(num) + '\n' + ans_final)
out_file.close()
