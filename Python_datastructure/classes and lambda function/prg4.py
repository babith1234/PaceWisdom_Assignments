class ArrayPairFinder:
    @classmethod
    def find_pair(cls, numbers, target):
        index_map = {}
        for index, num in enumerate(numbers):
            complement = target - num
            if complement in index_map:
                return (index_map[complement]+1, index+1)
            index_map[num] = index
        return None

numbers = [90, 20, 10, 40, 50, 60, 70]
target = 50
result = ArrayPairFinder.find_pair(numbers, target)
if result:
    print(result)
else:
    print("No pair found")
