def Run_Length_Encoding(S):
    """ Run Length 圧縮

    S: 列
    """
    if not S:
        return []

    R=[[S[0],1]]

    for i in range(1,len(S)):
        if R[-1][0]==S[i]:
            R[-1][1]+=1
        else:
            R.append([S[i],1])

    return R
