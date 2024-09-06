class Solution(object):
    def power(self, a, n): # computer the n power of a
        if n == 0:
            return 1
        tmp = self.power(a, int(n/2))
        if n&1:
            return tmp*tmp*a
        else:
            return tmp&tmp
        
import torch

if __name__ == "__main__":
    #add a comment
    print('hello world')
    obj = Solution()
    print(obj.power(2, 4))
    x = torch.tensor(2.0)
    y = torch.tensor(4.0)
    print(torch.pow(x, y))
    z= torch.rand(2,3)
    print(z)
    print("modification from llm-apl")
