#Link :https://leetcode.com/problems/min-stack/
class MinStack(object):
    def __init__(self):
        self.st_list=[]
    def push(self, val):
       curMin=self.getMin()
       if curMin == None or curMin > val:
           curMin = val
       self.st_list.append((val,curMin))
    def pop(self):
        self.st_list.pop()
    def top(self):
        return self.st_list[-1][0] if self.st_list else None

    def getMin(self):
        return self.st_list[-1][1] if self.st_list else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()