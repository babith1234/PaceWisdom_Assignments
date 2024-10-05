class Subsets:
    @classmethod
    def find_subsets(cls, nums):
        result = []
        subset = []

        def backtrack(start):
            result.append(subset[:])  
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        
        backtrack(0)
        return result


nums = [4, 5, 6]
print(Subsets.find_subsets(nums))
