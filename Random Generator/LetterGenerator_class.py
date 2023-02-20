import random

# import modules for AlphaNumberList class.
from LetterList_class import AlphaNumberList

class LetterGenerator():

    @staticmethod
    def GenerateARandomNumber(minValue:int,maxValue:int): # Inclusive minValue , Exclusive maxValue
        rdf=random.random()
        return int(rdf*(maxValue-minValue)+minValue)
    
    @staticmethod
    def GenerateARandomLetter(): 
        rdn=LetterGenerator.GenerateARandomNumber(minValue=0, maxValue=len(AlphaNumberList.GetList()))
        return AlphaNumberList.GetList()[rdn]
    
    @staticmethod
    def GenerateRandomList(minElem:int,maxElem:int)->list:
        numOfElem=LetterGenerator.GenerateARandomNumber(minElem,maxElem)
        li=[ LetterGenerator.GenerateARandomLetter() for k in range(0,numOfElem,1)]
        return li
    
    @staticmethod
    def GenerateRandomTuple(minElem,maxElem)->tuple:
        numOfElem=LetterGenerator.GenerateARandomNumber(minElem,maxElem)
        tu=tuple(LetterGenerator.GenerateARandomLetter() for k in range(0,numOfElem,1))
        return tu
    
    @staticmethod
    def GenerateRandomSet(minElem,maxElem)->set:
        numOfElem=LetterGenerator.GenerateARandomNumber(minElem,maxElem)
        se={LetterGenerator.GenerateARandomLetter() for k in range(0,numOfElem,1)}
        return se
    
    @staticmethod
    def GenerateRandomDict(minElem,maxElem)->dict:
        numOfElem=LetterGenerator.GenerateARandomNumber(minElem,maxElem)
        dic=dict()
        for k in range(0,numOfElem,1):
            d={LetterGenerator.GenerateARandomLetter():LetterGenerator.GenerateARandomLetter()}
            dic.update(d)
            return dic

    
    
    @staticmethod
    def GenerateRandomNestedData(minElem:int,maxElem:int,level:int):
        
        # Hidden variables
        __func_list=[LetterGenerator.GenerateRandomList
                     ,LetterGenerator.GenerateRandomTuple
                     ,LetterGenerator.GenerateRandomDict]
        __wrapper_list=[list
                        ,tuple
                        ,dict] 
        
        if level == 1:
            rdn = LetterGenerator.GenerateARandomNumber(0,len(__func_list)-1+1)
            randomFunc=__func_list[rdn]
            randomData=randomFunc(minElem,maxElem)
            return randomData
        else:
            rdn = LetterGenerator.GenerateARandomNumber(0,len(__func_list)-1+1)
            randomData=LetterGenerator.GenerateRandomNestedData(minElem,maxElem,level = 1)
            randomNestedData=LetterGenerator.GenerateRandomNestedData(minElem,maxElem,level = level - 1)
            print(randomData)
            print("~~~~~~~~~~~~~~~~~~~~~~~~")
            print(randomNestedData)
            if isinstance(randomData,(list)):
                randomData=[randomData,randomNestedData]
                return randomData
            """
            There are issues about hashes.
            if isinstance(randomData,(set)):
                randomData={randomData,randomNestedData}
                return randomData
            """
            if isinstance(randomData,(tuple)):
                randomData=(randomData,randomNestedData)
                return randomData
            if isinstance(randomData,(dict)):
                randomDict={LetterGenerator.GenerateARandomLetter():randomNestedData}
                randomData.update(randomDict)
                return randomData
        
 
# Example
def test():
    minElem=2
    maxElem=5
    minValue=2
    maxValue=5
    level=3
    li=LetterGenerator.GenerateRandomNestedData(minElem=minElem,maxElem=maxElem,level = level)
    print(li)

if __name__=='__main__':
    test()