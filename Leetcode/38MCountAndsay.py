# When I first read the question, I don't really understand what is this question meaning. Actually it is very simple.
# Everthing start 1, 1 is 1, nothing else.
# Then we go to the next one. If we wanna know this result, we need to count the previous result, which is "1". That's why the title of the question is "Count and Say". The last result is "1", just one "1", so this result is "11"
# Now we keep going, the last result is "11", so there are 2 "1" in the result, so this time the result is "21".
# For this time, we know last result is "21", which means there are one "2" and one "1", the result is "1211"
# ....
# Now we do a test, if the (n-1)th result is "12212333312111238"(I typed it randomly), what is the n th result? Let's count it. one "1", two "2", one "1" , one "2" , four"3" , one "1" , one "2", three"1", one "2", one"3" and one "8".Therefore, the result is "1122111243111231121318"
# Obviously, if we wanna know the n th result, we just need to count the (n - 1)th result, and the first result is "1". No explanation.

# hopes this saves your lot of time...........

class Solution(object):
    def func(self, n):
        if n == 1:
            return '1'
        res = None

        prev = None

        if n == 2:
            return '11'

        if n > 2:
            res = '11'
        count = 0


        for i in range(n-2):
            for j in res:
                if prev == None:
                    prev = 
                    count+=1

        # def recur(n):
        #     if n == 1:
        #         res = '1'

        res = None

        return res


sln = Solution()
print(sln.func(4))
