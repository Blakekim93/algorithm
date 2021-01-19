import re

class Solution:
    def isPalindrome(self, s: str):
        alpha = re.compile('[a-zA-Z0-9]')
        result = ''
        for i in s:
            if alpha.match(i) != None:
                result += i
        
        result = ''.join(list(result.lower()))
        reverse = ''.join(list(reversed(result)))
                
        if result == reverse:
            return True
        else:
            return False
