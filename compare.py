import filecmp
target = 0
all_in = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
all_out = ["a.out", "b.out", "c.out", "d.out", "e.out"]
compare_file = "test.out"
print(filecmp.cmp(compare_file, all_out[target]))
