class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        signature_s = [0] * 26
        signature_t = [0] * 26
        for i in s:
            signature_s[ord(i) - 97] += 1
        for i in t:
            signature_t[ord(i) - 97] += 1
            
        return signature_s == signature_t