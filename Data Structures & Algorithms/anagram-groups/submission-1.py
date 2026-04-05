class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        dict = {} 

        for x in strs:

            temp = [0] * 26

            for y in x:
                temp[ ord(y) - 97 ] = temp[ ord(y) - 97 ] + 1
            
            hash = tuple(temp)

            if(hash not in dict):
                dict[hash] = []
                dict[hash].append(x)
            else:
                dict[hash].append(x)
        
        ans = []
        for x in dict:
            ans.append(dict[x])
        
        return ans

    