class Sums():
    def two_sums(self, nums, target):
        self.nums = nums
        self.target = target
        
        dict = {}
        for i, j in enumerate(self.nums):
            if self.nums[i] in dict:
                return [dict[self.nums[i]], i]
            else:
                dict[self.target - self.nums[i]] = i

instance =  Sums()
print(instance.two_sums([2,3,5,2,4,54,57,34,34], 111))
