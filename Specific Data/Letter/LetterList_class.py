
class NumbersList():
    li=[]     
    @staticmethod
    def GetList():
        NumbersList.li.extend([ chr(c) for c in range(48,57+1,1)])
        return NumbersList.li
        
class AlphaLowercaseList():
    li=[]     
    @staticmethod
    def GetList():
        AlphaLowercaseList.li.extend([ chr(c) for c in range(97,122+1,1)])
        return AlphaLowercaseList.li
      
class AlphaUppercaseList():
    li=[]     
    @staticmethod
    def GetList():
        AlphaUppercaseList.li.extend([ chr(c) for c in range(65,90+1,1)])
        return AlphaUppercaseList.li
        
class AlphaList():
    li=[]     
    @staticmethod
    def GetList():
        AlphaList.li.extend([ chr(c) for c in range(65,90+1,1)])
        AlphaList.li.extend([ chr(c) for c in range(97,122+1,1)])
        return AlphaList.li
        
class AlphaNumberList():
    li=[]     
    @staticmethod
    def GetList():
        AlphaNumberList.li.extend([ chr(c) for c in range(48,57+1,1)])
        AlphaNumberList.li.extend([ chr(c) for c in range(65,90+1,1)])
        AlphaNumberList.li.extend([ chr(c) for c in range(97,122+1,1)])
        return AlphaNumberList.li

# Test data
def test():
    print(NumbersList.GetList())
    print(AlphaLowercaseList.GetList())
    print(AlphaUppercaseList.GetList())
    print(AlphaList.GetList())
    print(AlphaNumberList.GetList())

if __name__=='__main__':
    test()