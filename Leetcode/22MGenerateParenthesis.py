# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]


class solution:
    def gen(self, n):
        res = set()

        def backtrack(l, r, st):

            if l == n and r == n and l == r:
                res.add(st)
                return
            if l < n:
                st = st + "("
                backtrack(l + 1, r, st)
                st = st[:-1]

            if r < l:
                st = st + ")"
                backtrack(l, r+1, st)
                st = st[:-1]

        backtrack(0, 0, "")

    def gen2(self, n):
        res = set()

        def backtrack(l, r, st):
            if l == n and r == n and l == r:
                res.add(st)
                return
            if l < n:
                backtrack(l + 1, r, st + "(")
                

            if r < l:
                backtrack(l, r+1,  st + ")")
                

        backtrack(0, 0, "")
        return res


sln = solution()
print(sln.gen2(3))

# print(sln.res)
# print(sln.res1)
