from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    my_list = []
    nums.sort()
    for index, n in enumerate(nums):
        next_index = index + 1
        last = len(nums) - 1

        if index > 0 and n == nums[index - 1]:
            continue
        while next_index < last:
            total = n + nums[next_index] + nums[last]
            if total > 0:
                last -= 1
            elif total < 0:
                next_index += 1
            else:
                is_zero = [n, nums[next_index], nums[last]]
                my_list.append(is_zero)
                next_index += 1
                while nums[next_index] == nums[next_index - 1] and next_index < last:
                    print(next_index)
                    next_index += 1
    return my_list


input = [2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]
new_input = input
new_input.sort()
print(new_input)
output = threeSum(input)
expect = [[-10, 5, 5], [-5, 0, 5], [-4, 2, 2], [-3, -2, 5], [-3, 1, 2], [-2, 0, 2]]

if output == expect:
    print("Done")
else:
    print("Failed")
