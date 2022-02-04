# Ritik Kumar
# Task4 Day4 of Python Zero to Hero Program

n=int(input())
def GetFactorial(N):
    if(N==1):
        return 1
    else:
        return N* GetFactorial(N-1)



print(GetFactorial(n))