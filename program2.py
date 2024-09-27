 def romanToDecimal(self, S): 
        # code here
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        n=len(S)
        
        for i in range(n):
            if i < n-1 and roman_dict[S[i]] < roman_dict[S[i+1]]:
                num-=roman_dict[S[i]]
            else:
                num+=roman_dict[S[i]]
        return num
