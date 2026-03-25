def combinations(arr, n):
    result = []

    def dfs(start, current):
        print("current", current, "result", result)
        if len(current) == n:
            result.append(current[:])
            return

        for i in range(start, len(arr)):
            current.append(arr[i])
            dfs(i + 1, current)
            current.pop()

    dfs(0, [])
    return result

print(combinations([1, 2, 3], 2))