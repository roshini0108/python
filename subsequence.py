"""def PrintSbsq(s,i,res):
    if i==len(s):
        print(res)
        return
    # include the character at index i
    PrintSbsq(s,i+1,res+s[i])
    # exclude the character at index i
    PrintSbsq(s,i+1,res)
print("subsequence")
PrintSbsq("suji",0,"")"""
# longest common subsequence
class Python: 
    def __init__(self):
        self.res=''

    def printn(self):
        print(self.res)

    def lcs(self, s1, s2, i, j):
        if i == len(s1) or j == len(s2):
            return ''
        if s1[i] == s2[j]:
            return s1[i] + self.lcs(s1, s2, i+1, j+1)
        else:
            x = self.lcs(s1, s2, i+1, j)
            y = self.lcs(s1, s2, i, j+1)
            return x if len(x) > len(y) else y

p = Python()  
print("Longest Common Subsequence:")
print(p.lcs("kavya", "kavitha", 0, 0))
