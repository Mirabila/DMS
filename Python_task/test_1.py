def solve(nums: list[int], target: int) -> list[int]:
    dict = {}
    for index, val in enumerate(nums):
        if dict.get(target - val) != None:
            return [dict.get(target - val), index]
        elif dict.get(val) == None:
            dict.update({val:index})

