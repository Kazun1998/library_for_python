def Convolution(A,B):
    def FFT(A, inverse=False):
        from math import sin,cos,pi
        N=len(A)
        max_level=N.bit_length()-1

        w=complex(cos(2*pi/N), sin(2*pi/N))

        if inverse: #逆変換ならば...
            w=w.conjugate() #逆元

        W=[0]*(max_level+1)
        W[-1]=w

        for k in range(max_level-1,-1,-1):
            W[k]=W[k+1]*W[k+1]

        def fft(X, level):
            t=len(X)
            if t==1:
                return X

            Y=[0]*(t>>1)
            Z=[0]*(t>>1)

            w=W[level]
            u=1
            for j in range(t//2):
                Y[j]=X[j]+X[j+t//2]
                Z[j]=(X[j]-X[j+t//2])*u
                u*=w

            Y=fft(Y, level-1)
            Z=fft(Z, level-1)

            V=[0]*t
            for k in range(t>>1):
                V[2*k]=Y[k]
                V[2*k+1]=Z[k]
            return V

        return fft(A, max_level)

    def Inverse_NTT(A):
        B=FFT(A, True)
        N=len(A)
        return [b/N for b in B]
    from math import floor

    #========================================

    if len(A)==0 or len(B)==0:
        return 0

    L=len(A)+len(B)-1
    N=1<<((len(A)+len(B)-1)-1).bit_length()
    A=A+[0]*(N-len(A))
    B=B+[0]*(N-len(B))

    A=FFT(A); B=FFT(B)
    A=[A[i]*B[i] for i in range(N)]
    A=Inverse_NTT(A)

    del A[L:]
    return [floor(a.real+0.5) for a in A]
