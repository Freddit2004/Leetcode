1
2class Solution:
3    def longestCommonPrefix(self, strs: List[str]) -> str:
4        if not strs:
5            return ""
6        
7        prefix = strs[0]
8        
9        for s in strs[1:]:
10            i = 0
11            # compare characters one by one
12            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
13                i += 1
14            
15            prefix = prefix[:i]  # keep only matching part
16            
17            if prefix == "":
18                return ""
19        
20        return prefix
21        