class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        chars_count = {}

        left = 0
        
        maxfreq = 0
        maxlen = 0

        for right in range(len(s)):

            if s[right] not in chars_count:
                chars_count[s[right]] = 1
            else:
                chars_count[s[right]] += 1
            
            if(maxfreq < chars_count[s[right]]):
                maxfreq = chars_count[s[right]]
            
            if (right - left + 1) - maxfreq > k:
                chars_count[s[left]] -= 1
                left += 1
            
            cur_length = right - left + 1
            maxlen = max(cur_length,maxlen)
        
        return maxlen