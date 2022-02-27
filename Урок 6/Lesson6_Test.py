import numpy as np

# print(100 / np.log(100))

def sieve(num):
    if num == 1:
        return 2

    num_list = [i for i in range(10 ** num)]
    num_list[1] = 0
    i = 2
    s_num_list = []
    while len(s_num_list) < num:
        if num_list[i] != 0:
            s_num_list.append(num_list[i])
            j = i * 2
            while j < len(num_list):
                num_list[j] = 0
                j += i
        i += 1
    return s_num_list[-1]

# n = 100
# lst = [i for i in range(n * n)]

print(sieve(25))