class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # output = ""
        # get first
        # for char in first
        # check i, char in all strs
        
        # output += chars
        # if char not in strs: pass
        # prefix: index of char == word[i]
        output = ""
        first = strs[0]
        for i, char in enumerate(first):
            count = 0
            for word in strs:
                if i < len(word):
                    if char in word and word[i] == char:
                        count += 1
                    else:
                        return output
            if count == len(strs):
                output += char
            
        return output
            


    
