class Solution(object):
    def power(self, a, n): # computer the n power of a
        if n == 0:
            return 1
        tmp = self.power(a, int(n/2))
        if n&1:
            return tmp*tmp*a
        else:
            return tmp&tmp

if __name__ == "__main__":
    #add a comment
    print('hello world')
    obj = Solution()
    print(obj.power(2, 4))