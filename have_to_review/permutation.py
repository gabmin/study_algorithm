def permutation(arr, r):
    result = []

    def dfs(current, visited):
        if len(current) == r:
            result.append(current[:])
            return

        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                current.append(arr[i])
                dfs(current, visited)
                current.pop()
                visited[i] = False

    dfs([], [False] * len(arr))
    return result

print(permutation([1, 2, 3], 2))