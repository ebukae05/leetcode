#class
class MyClass:
    #constructor
    def __init__(self, nums):
        #member variables
        self.nums = nums
        self.size = len(nums)
    
    #methods
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()