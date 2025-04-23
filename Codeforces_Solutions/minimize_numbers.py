# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P
# Mem 200 KB
# Solution 1 took 62 ms	, Solution 2 took 77 ms


######## Solution 1 ########
def minimize_nums(n, nums):
    result_set = []
    for i in range(n):
        result_set.append(count_divisions_by_2(0, nums[i]))
    return min(result_set)


def count_divisions_by_2(counter, num):
    if num % 2 != 0:
        return counter
    return count_divisions_by_2(counter + 1, num // 2)


n = int(input())
nums = list(map(int, input().split()))

print(minimize_nums(n, nums))


######## Solution 2 ########


def minimize_nums(n, nums):
    counter = 1
    while counter:
        remainder_list = []
        for i in range(n):
            if nums[i] % 2 != 0:
                return counter - 1
            else:
                remainder_list.append(nums[i] // 2)
        nums = remainder_list
        counter = counter + 1


n = int(input())
nums = list(map(int, input().split()))

print(minimize_nums(n, nums))
