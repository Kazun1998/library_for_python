def Manacher(S) -> list[int]:
    i = j = 0
    res = [0] * len(S)
    while i < len(S):
        while (i - j >= 0) and (i + j < len(S)) and (S[i - j] == S[i + j]):
            j += 1

        res[i] = j
        k = 1
        while (i - k >= 0) and (k + res[i - k] < j):
            res[i + k] = res[i - k]
            k += 1

        i += k; j -= k

    return [2 * x - 1 for x in res]

def Manacher_with_even(S, dummy = None) -> tuple[list[int], list[int]]:
    T = [dummy] * (2 * len(S) - 1)
    for i in range(len(S)):
        T[2 * i] = S[i]

    res = [(y + 1) // 2 for y in Manacher(T)]

    odd = [0] * len(S)
    for i in range(len(S)):
        odd[i] = res[2 * i] if res[2 * i] % 2 == 1 else res[2 * i] - 1

    even = [0] * (len(S) - 1)
    for i in range(len(S) - 1):
        even[i] = res[2 * i + 1] if res[2 * i + 1] % 2 == 0 else res[2 * i + 1] - 1

    return odd, even
