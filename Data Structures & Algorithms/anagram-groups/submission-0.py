class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = [[strs[0]]]
        for i in strs[1:]:
            flag = True
            for x in range(len(groups)):
                if self.isAnagrams(groups[x][0], i):
                    groups[x].append(i)
                    flag = False
                    break
            if flag:
                groups.append([i])
        return groups


    def isAnagrams(self, s, t):
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        