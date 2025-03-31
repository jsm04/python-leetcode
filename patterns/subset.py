def subsets(nums: list[int]):
    res = []

    def backtrack(start, path):
        print(f"Path before appending: {path}")
        res.append(path[:])  # Store current subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            print(f"Adding {nums[i]}, path now: {path}")
            backtrack(i + 1, path)
            path.pop()
            print(f"Backtracking, path after removing {nums[i]}: {path}")

    backtrack(0, [])
    return res


# print(subsets([1, 2, 3]))


def bitmask_subsets(nums: list[int]):
    res = []
    n = len(nums)
    for mask in range(1 << n):  # 2^n subsets
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        res.append(subset)
    return res


print(bitmask_subsets([1, 2, 3]))
