import random

# import modules for AlphaNumberList class.

def GenerateARandomNumber(minValue:int,maxValue:int): # Inclusive minValue , Exclusive maxValue
    rdf=random.random()
    return int(rdf*(maxValue-minValue)+minValue)
def GenerateARandomLetter(): 
    rdn=GenerateARandomNumber(minValue=0, maxValue=len(junk2.AlphaNumberList.GetList()))
    return junk2.AlphaNumberList.GetList()[rdn]
def GenerateRandomList(minElem:int,maxElem:int)->list:
    numOfElem=GenerateARandomNumber(minElem,maxElem)
    li=[ GenerateARandomLetter() for k in range(0,numOfElem,1)]
    return li
def GenerateRandomTuple(minElem,maxElem)->tuple:
    numOfElem=GenerateARandomNumber(minElem,maxElem)
    tu=tuple(GenerateARandomLetter() for k in range(0,numOfElem,1))
    return tu
def GenerateRandomSet(minElem,maxElem)->set:
    numOfElem=GenerateARandomNumber(minElem,maxElem)
    se={GenerateARandomLetter() for k in range(0,numOfElem,1)}
    return se
def GenerateRandomDict(minElem,maxElem)->dict:
    numOfElem=GenerateARandomNumber(minElem,maxElem)
    dic=dict()
    for k in range(0,numOfElem,1):
        d={GenerateARandomLetter():GenerateARandomLetter()}
        dic.update(d)
    return dic

func_list=[GenerateRandomList,GenerateRandomTuple,GenerateRandomDict]

wrapper_list=[list,tuple,dict]

def GenerateRandomNestedData(minElem:int,maxElem:int,level:int):
    if level == 1:
        rdn = GenerateARandomNumber(0,len(func_list)-1+1)
        randomFunc=func_list[rdn]
        randomData=randomFunc(minElem,maxElem)
        return randomData
    else:
        rdn = GenerateARandomNumber(0,len(func_list)-1+1)
        randomData=GenerateRandomNestedData(minElem,maxElem,level = 1)
        randomNestedData=GenerateRandomNestedData(minElem,maxElem,level = level - 1)
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
            randomDict={GenerateARandomLetter():randomNestedData}
            randomData.update(randomDict)
            return randomData
        
"""
# Example
minElem=2
maxElem=5
minValue=2
maxValue=5
level=3
li=GenerateRandomNestedData(minElem=minElem,maxElem=maxElem,level = level)
print(li)
"""
