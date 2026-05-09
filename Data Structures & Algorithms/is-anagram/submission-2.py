class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mem = [0]*26

        for a in s:
            mem[ord(a) - 97] += 1

        for a in t:
            if mem[ord(a) - 97] > 0:
                mem[ord(a) - 97] -= 1
            else:
                return False
        for i in mem:
            if i > 0:
                return False
            
        return True
