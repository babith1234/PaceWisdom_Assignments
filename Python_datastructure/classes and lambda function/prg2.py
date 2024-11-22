class Strings:
    dict={
        '(':')', '[':']','{':'}'
        }
    @classmethod
    def valdity(cls,s):
        list=[]
        for char in s:
            if char in cls.dict:
                list.append(char)
            elif list and cls.dict[list[-1]]==char:
                list.pop()
            else:
                return False
        return len(list)==0
    
s="({[)]"
print(Strings.valdity(s))
            
    