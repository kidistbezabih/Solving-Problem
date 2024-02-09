class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alphabets = {'a':0,'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6,
                    'h':7,'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13,
                    'o':14,'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 
                    'v':21,'w':22, 'x':23, 'y':24, 'z':25}
        ln =  len(s)
        lis = [0]*ln
        for st, e, d in shifts:
            if d == 0:
                lis[st] -= 1
                if e +1< ln:
                   lis[e+1] +=1
            else:
                lis[st] += 1
                if e +1< ln:
                   lis[e+1] -=1
        for i in range(1,ln):
            lis[i] += lis[i-1]

        for i in range(ln):
            lis[i] = (lis[i] + alphabets[s[i]])%26
            lis[i] = list(alphabets.keys())[lis[i]]
        
        return ''.join(lis)
