def backtrack(curr, pos, trgt):
    if trgt == 0 and curr not in result:
        result.append(curr[:])
        return

    for i in range(pos, len(candidates)):
        if candidates[i] > trgt:
            break
        curr.append(candidates[i])
        backtrack(curr, i + 1, trgt - candidates[i])
        curr.pop()

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
result = []
candidates.sort()
backtrack([], 0, target)
print(result)