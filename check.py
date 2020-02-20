# check if an answer is valid
target = [0, 1, 2, 3, 4]
all_in = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
all_out = ["a.out", "b.out", "c.out", "d.out", "e.out"]

for test in target:
    print(test)
    in_file = open(all_in[test], "r")
    first_line = in_file.readline()
    second_line = in_file.readline()
    in_file.close()
    m, n = list(map(int, first_line.split(" ")))
    s = list(map(int, second_line.split(" ")))

    out_file = open(all_out[test], "r")
    first_line = out_file.readline()
    second_line = out_file.readline()
    out_file.close()
    num = int(first_line)
    ans_list = list(map(int, second_line.split(" ")))
    sum_check = 0

    err = 0
    if num > n:
        err = 1
        print("Error at 1:")
        print(num)
        print(n)
    for i in range(len(ans_list)):
        if ans_list[i] >= len(s):
            err = 2
            print("Error at 2:")
            print(ans_list[i])
            print(len(s))
            break
        if i > 0 and ans_list[i] <= ans_list[i - 1]:
            err = 3
            print("Error at 3:")
            print(ans_list[i])
            print(ans_list[i - 1])
            break
        sum_check += s[ans_list[i]]
    if sum_check > m:
        err = 4
        print("Error at 4:")
        print(sum_check)
        print(m)
    if len(ans_list) != num:
        err = 5
        print("Error at 5:")
        print(len(ans_list))
        print(num)

    print(sum_check)
    print(err)
