class Solution(object):
    def containsDuplicate(self,nums):
        seen = {}
        for num in nums:
            if num in seen: #if there is a duplicate in the seen array return true
                print(seen)           
                return True 
            
            else:
                seen[num]=1 # 1 is the value of the key 
        return False 


# Example usage
# arr = [1, 2, 3, 4, 5]
# sol = Solution()
# print(sol.containsDuplicate(arr)) # Output: False


arr = [20, 8, 8, 6, 5, 20]
sol = Solution() #create a new instance of the class

print(sol.containsDuplicate(arr)) # Output: True


