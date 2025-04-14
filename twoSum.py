from typing import List

nums = [2,7,11,15]
target = 9

def twoSum(nums: List[int], target: int) -> List[int]:
    for i, j in enumerate(nums):
        if j + nums[i+1] == target:
            ans = [i, i+1]
            print(ans)
            return ans
        else:
            pass
twoSum(nums=nums, target=target)


def twoSum_v2(nums: List[int], target: int) -> List[int]:
    lst = []
    for i, j in enumerate(nums):
        x = target - j
        print(f"{x} = {target} - {j}")
        nxt = i+1
        if x + nxt == target:
            print(f"{x}+{nums[i]}={target}")
            lst.append(i)
            lst.append(nxt)
    print(lst)
    pass

# twoSum_v2(nums=nums, target=target)


def twoSum_v3(nums: List[int], target: int) -> List[int]:
    lst = []
    nums_count = len(nums)
    for x in range(0, nums_count):
        for i, j in enumerate(nums):
            if j + nums[i+1] == target:
                print("winner")
                pass

# twoSum_v3(nums=nums, target=target)