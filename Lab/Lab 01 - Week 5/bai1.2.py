import math
def N_to_Binary(N):
    print("\nVoi N = ", N, "thi:")

    sum = 0
    count = -1
    log_2_N = math.log2(N)

    # Gan(N), Sosanh(N)
    count_gan = 3
    count_sosanh = 1

    while (N != 0):
        count_sosanh += 1
        count += + 1
        sum = sum + (N % 2) * pow(10, count)
        N = N // 2
        count_gan += 3

    print(sum)
    print("So phep so sanh: ", count_sosanh)
    print("so phep gan: ", count_gan)

    return log_2_N, count_gan, count_sosanh

import numpy as np
N = np.array([100,200,300,400,500,600,700,800,900,1000])
y = []

for i in N:
    index = int((i/100)-1)
    print(index)
    y.append(N_to_Binary(i))

y_new = np.array(y)
