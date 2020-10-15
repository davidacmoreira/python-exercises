def array_manipulation(n, queries):
    arr = [0]*n

    for a, b, k in queries:
        arr[a-1] += k
        if b != n:
            arr[b] -= k

    max_sum = 0
    value_sum = 0

    for i in range(n):
        value_sum += arr[i]
        if value_sum > max_sum:
            max_sum = value_sum

    return max_sum


n = 5
m = 3

queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]  # 200

print(array_manipulation(n, queries))
