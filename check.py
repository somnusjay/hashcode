# check if an answer is valid
target = 2
all_in = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
all_out = ["a.out", "b.out", "c.out", "d.out", "e.out"]

in_file = open(all_in[target], "r")
first_line = in_file.readline()
second_line = in_file.readline()
in_file.close()
m, n = list(map(int, first_line.split(" ")))
s = list(map(int, second_line.split(" ")))

out_file = open(all_out[target], "r")
first_line = out_file.readline()
second_line = out_file.readline()
out_file.close()
num = int(first_line)
ans_list = list(map(int, second_line.split(" ")))

sum_check = 0
err = False
if num > n:
    err = True
for i in ans_list:
    if i > len(s):
        err = True
        break
    sum_check += s[i]
if sum_check > m:
    err = True

if err:
    print("Error!")
else:
    print("Valid!")
