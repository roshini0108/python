def PrintSbsq(s,i,res):
    if i==len(s):
        print(res)
        return
    # include the character at index i
    PrintSbsq(s,i+1,res+s[i])
    # exclude the character at index i
    PrintSbsq(s,i+1,res)
    print("subsequence")