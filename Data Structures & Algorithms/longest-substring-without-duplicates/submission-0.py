class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dict = {}

        left = 0
        right = 0
        max = 0
        count = 0
        
  
        while right < len(s): 
            
            if s[right] not in dict or dict[s[right]] < left:
                dict[s[right]] = right
                right += 1
                count += 1
            else:
                
                left = dict[s[right]] + 1
                count = right - left + 1
                dict[s[right]] = right
                right += 1
            
            
            if(count > max):
                max = count
                
        return max