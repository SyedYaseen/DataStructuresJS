class Solution:
    def isAnagram(self, mem, anagWord):
        for ch in anagWord:
                    if ch not in mem or mem[ch] == 0:
                        break
                    else:
                        mem[ch] -= 1

    def groupAnagrams(self, strs: list):
        for word in strs:
            current = [word]
            strs.remove(word)
            mem = {}
            for ch in word:
                if ch in mem:
                    mem[ch] +=1
                else:
                    mem[ch] = 1
            
            for anagWord in strs:
                compareMem = mem.copy()
                if self
                


    






sln = Solution()
print(sln.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
