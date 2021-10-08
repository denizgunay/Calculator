class Calculator(object):
        
    def order(self,x):  #this function provides the priority of parantheses.        
        openIndex = [i for i in range(len(x)) if x[i] == '('][-1] +1
        closeIndex = x.index(')')
        return (openIndex,closeIndex)
    
    def detector(self,n,i,rev = False): #this function detects the numbers.
        if rev == False:
            num = n[i]
            while i < len(n)-1:
                if n[i+1].isnumeric() or n[i+1] == '.':
                    num += n[i+1]
                    i+=1
                else:
                    break
            return (float(num),i+1) if '.' in num else (int(num),i+1)
    
        elif rev == True:
            num = n[i]
            while i > 0:
                if n[i-1].isnumeric() or n[i-1] == '.':
                    num += n[i-1]
                    i -= 1
                else:
                    break
            return (float(num[::-1]),i) if '.' in num else (int(num[::-1]),i)
        
    def operator(self,x): #this function does the main calculation.                        
        while '*' in x or '/' in x:
            k = [i for i in range(len(x)) if x[i] == '*' or x[i] == '/']
            for i in k:
                abc = self.detector(x,i-1,True)
                bce = self.detector(x,i+1,False)
                num1 = abc[0]
                a = abc[1]
                num2 = bce[0]
                b = bce[1]
                if x[i] == '*':
                    result = num1*num2
                elif x[i] == '/':
                    result = num1/num2
                x = x[:a] + str(result) + x[b:]
                break
            continue                        
                    
        if x[0] != '-':
            v = [self.detector(x,0)[0]]
            u = [self.detector(x,i)[0] for i in range(self.detector(x,0)[1],len(x)) if x[i] == '-' or x[i] == '+']
            if '.' in str(sum(u+v)):            
                pointLoc = str(sum(u+v)).index('.')
                if int(str(sum(u+v))[pointLoc+1:]) == 0:
                    return int(sum(u+v))
                else:
                    return round(sum(u+v),3)
            else:
                return int(sum(u+v))
             
        else:
            u = [self.detector(x,i)[0] for i in range(len(x)) if x[i] == '-' or x[i] == '+']
            if '.' in str(sum(u)):            
                pointLoc = str(sum(u)).index('.')
                if int(str(sum(u))[pointLoc+1:]) == 0:
                    return int(sum(u))
                else:
                    return round(sum(u),3)
            else:
                return int(sum(u))        
                
    def evaluate(self,x): #and the last function gives the answer...
        x = x.replace(' ','') 
        while '(' in x:
            indexes = self.order(x)
            opIndex = indexes[0]
            clsIndex = indexes[1]
            result = self.operator(x[opIndex:clsIndex])
            x = x[:opIndex-1] + str(result) + x[clsIndex+1:]
        else:
            return self.operator(x)