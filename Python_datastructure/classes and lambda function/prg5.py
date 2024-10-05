class ZeroSumTriplets:
    @classmethod
    def find_triplets(cls, nums):
        nums.sort()
        triplets = []
        length = len(nums)

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return triplets

input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
result = ZeroSumTriplets.find_triplets(input_array)
print(result)
