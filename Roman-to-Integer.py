1class Solution:
2    def romanToInt(self, s: str) ->int:
3        roman = {
4            'I': 1, 'V': 5, 'X': 10,
5            'L': 50, 'C': 100,
6            'D': 500, 'M': 1000
7        }
8        
9        total = 0
10        
11        for i in range(len(s)):
12            # If current is smaller than next → subtract
13            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
14                total -= roman[s[i]]
15            else:
16                total += roman[s[i]]
17        
18        return total