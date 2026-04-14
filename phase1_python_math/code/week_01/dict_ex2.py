def factorials(n: int) -> dict[int, int]:
    fact_dict = {}
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        fact_dict[i] = factorial
    return fact_dict


k = factorials(5)

print(k[2])
print(k[4])
print(k[5])
