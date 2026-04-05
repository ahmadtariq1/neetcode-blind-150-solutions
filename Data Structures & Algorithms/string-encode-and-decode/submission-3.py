class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""
        for x in strs:
            s = s + str(len(x)) + "#" + x
        
        print(s)
        return s
        
    def decode(self, s: str) -> List[str]:
        j = 0
        ans = []
        while j < len(s):
            i = j

            while s[i] != "#":
                i += 1
            count = int(s[j:i])
            j = i + 1
            i = j + count
            temp = s[j:i]
            ans.append(temp)
            j = i


        return ans

        