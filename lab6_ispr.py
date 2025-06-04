import math
import timeit
import pandas as pd
import matplotlib.pyplot as plt

def F_G_recursive(n: int):
    if n == 1:
        return 1.0, 1.0
    prev_F, prev_G = F_G_recursive(n - 1)
    sign = -1.0 if (n % 2 == 1) else 1.0
    F_n = sign * (prev_F - 2.0 * prev_G)
    G_n = -prev_F + math.factorial(2 * n - 1)
    return F_n, G_n

def F_G_iterative(n: int):
    F_prev = 1.0
    G_prev = 1.0
    fact = 1
    for i in range(2, n + 1):
        # обновляем fact от (2*(i-1)-1)! до (2*i - 1)!
        start = 2 * (i - 1)
        end = 2 * i - 1
        for j in range(start, end + 1):
            fact *= j
        sign = -1.0 if (i % 2 == 1) else 1.0
        F_curr = sign * (F_prev - 2.0 * G_prev)
        G_curr = -F_prev + fact
        F_prev, G_prev = F_curr, G_curr
    return F_prev, G_prev

if __name__ == "__main__":
    results = []
    for n in range(2, 21):
        rec_time = timeit.timeit(lambda: F_G_recursive(n), number=10)
        itr_time = timeit.timeit(lambda: F_G_iterative(n), number=10)
        results.append((n, rec_time, itr_time))

    df = pd.DataFrame(results, columns=["n", "Recursive Time (s)", "Iterative Time (s)"])
    print("Сравнение времени выполнения")
    print(df.to_string(index=False))

    plt.figure(figsize=(8, 5))
    plt.plot(df["n"], df["Recursive Time (s)"], label="Рекурсивный", marker="o", color="orange")
    plt.plot(df["n"], df["Iterative Time (s)"], label="Итеративный", marker="o", color="red")
    plt.xlabel("n")
    plt.ylabel("Время выполнения (с)")
    plt.title("Сравнение рекурсивного и итеративного подходов")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()