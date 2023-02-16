# File name 
# string-to-any-type-class.py

## README

# test data for input and status of output shown in the following block.
# if __name__=='__main__': block.

# It just checkes the string is valid and 
# Strips the extra tab,newline,whitespace,single quote, double quote, parenthesis,square bracket, curly bracket.

# However, my code is NOT completed.
# I will complete the code so that it can achieve my goal as soon as possible.

# For more details, see README.md

from operator import itemgetter

from Letter_ENUM_class import Letter_ENUM
from Message_ENUM_class import Message_Enum
from Type_ENUM_class import Type_Enum
from Bracket_ENUM_class import Bracket_ENUM
from Quote_ENUM_class import Quote_ENUM

from ParenthesisProblem_class import ParenthesisProblem


class String2AnyType():
    def __init__(self):
        self.string=""
        
    def Print_Info(self,s,print_each_elem:bool):
        print("--------------------------------------------------------")
        
        if isinstance(s, (list,tuple,set)):
            if print_each_elem==True:
                for v in s:
                    print(v)
            else:
                print(s)
        else:
            print(s)
        print(type(s))
        if isinstance(s, (str,list,tuple,set)):
            print(len(s))
        
    def SetString(self,string:str):
        self.string=string
    
    def SplitString(self,s:str,delim:str)->str:
        result=s.split(delim)
        return result
    
    #### Original version
    
    def StripExtraQuote(self,s:str)->str:
        curr_s=s
        next_s=curr_s
        while True:
            next_s=curr_s.strip(Letter_ENUM.doubleQuote).strip(Letter_ENUM.singleQuote)
            if next_s == curr_s:
                return next_s
            curr_s = next_s
    
    #### Original version
      
    def StripExtraSpace(self,s:str)->str:
        curr_s=s
        next_s=curr_s
        while True:
            next_s=curr_s.strip(Letter_ENUM.whitespace).strip(Letter_ENUM.newline).strip(Letter_ENUM.tab)
            if next_s == curr_s:
                return next_s
            curr_s = next_s
        
    def StripExtraSpaceAndQuote(self,s:str)->str:
        curr_s=s
        next_s=curr_s
        
        while True:
            next_s=self.StripExtraQuote(curr_s)
            next_s=self.StripExtraSpace(next_s)
            if next_s==curr_s:
                return next_s
            curr_s=next_s
            
    def StripExtraSquareBracket(self,s:str)->str:
        if (s.startswith(Bracket_ENUM.pair[0][0]) and s.endswith(Bracket_ENUM.pair[0][1])):
            s=s.lstrip(Bracket_ENUM.pair[0][0]).rstrip(Bracket_ENUM.pair[0][1])
        return s
    
    def StripExtraCurlyBracket(self,s:str)->str:
        if (s.startswith(Bracket_ENUM.pair[2][0]) and s.endswith(Bracket_ENUM.pair[2][1])):
            s=s.lstrip(Bracket_ENUM.pair[2][0]).rstrip(Bracket_ENUM.pair[2][1])
        return s
    
    def StripExtraParenthesis(self,s:str)->str:
        if (s.startswith(Bracket_ENUM.pair[1][0]) and s.endswith(Bracket_ENUM.pair[1][1])):
            s=s.lstrip(Bracket_ENUM.pair[1][0]).rstrip(Bracket_ENUM.pair[1][1])
        return s
    
    def StripBracket(self,s:str)->str:
        curr_s=s
        temp_s=curr_s
        next_s=curr_s
        bracketIdx=-1
        while True:
            temp_s=curr_s
            
            next_s=self.StripExtraSquareBracket(temp_s)
            if next_s!=temp_s:
                bracketIdx=Type_Enum.INDEX_LIST
            temp_s=next_s
            
            next_s=self.StripExtraParenthesis(temp_s)
            if next_s!=temp_s:
                bracketIdx=Type_Enum.INDEX_TUPLE
            temp_s=next_s
            
            next_s=self.StripExtraCurlyBracket(temp_s)
            if next_s!=temp_s:
                bracketIdx=Type_Enum.INDEX_SET
            temp_s=next_s
            
            if next_s==curr_s:
                return (next_s,bracketIdx)
            
            curr_s=next_s
            temp_s=next_s

       
    def SplitAllBrackets_String2List(self,s:str)->list:
        
       pairIndex= [ 
                     [
                       [
                         (index,Bracket_ENUM.pair[row][col]) for index in range(0,len(s),1) if s.startswith(Bracket_ENUM.pair[row][col], index)
                        
                       ] 
                           for row in range(0,len(Bracket_ENUM.pair),1) 
                      
                     ] 
                         for col in range(0,len(Bracket_ENUM.pair[0]),1) 
            
                  ] 
       pairIndex=self.ConvertPair2Pair_ForBracket(pairIndex=pairIndex,flag=False)
       return pairIndex
    
    def SplitAllQuote_String2List(self,s:str)->list:
        pairIndex= [ 
                      [
                        [
                          (index,Quote_ENUM.pair[row][col]) for index in range(0,len(s),1) if s.startswith(Quote_ENUM.pair[row][col], index)
                         
                        ] 
                            for row in range(0,len(Quote_ENUM.pair),1) 
                       
                      ] 
                          for col in range(0,len(Quote_ENUM.pair[0]),1) 
             
                   ] 
        #pairIndex=self.ConvertPair2Pair_ForQuote(pairIndex=pairIndex,flag=False)
        return pairIndex
    
    def ConvertPair2Pair_ForBracket(self,pairIndex:list,flag:bool)->list:
        
        self.CheckParenthesisMismatched(pairIndex)
        
        result=list()
        for idx in range(0,len(pairIndex[0]),1):
            if len(pairIndex[0][idx])==0:
                if flag==True:
                    result.append([])                             
            else:
                for jdx in range(0,len(pairIndex[0][idx]),1):
                    result.append([pairIndex[0][idx][jdx],pairIndex[1][idx][jdx]])
        return result
    
    def ConvertPair2Pair_ForQuote(self,pairIndex:list,flag:bool)->list:
        pairIndex=pairIndex[0]
        #self.Print_Info(s=pairIndex, print_each_elem=False)
        return pairIndex
    
    def CheckParenthesisMismatched(self,pairIndex:list):
        for idx in range(0,len(pairIndex[0]),1):
            leftIdx=pairIndex[0][idx]
            rightIdx=pairIndex[1][idx]
            if len(leftIdx) != len(rightIdx):
                raise ValueError("ERROR!!! Mismatched Parenthesis.")
                
            
    def CheckNoBracket(self,pairIndex:list,options:list):
        
        if options[0]==True:            
            print("In the method CheckNoBracket,")
            print("pairIndex=")
            self.Print_Info(s=pairIndex, print_each_elem=False)
        
        p_len=len(pairIndex)
        # != 2
        if p_len != 2 :
            
            # > 2
            if p_len > 2:
                raise ValueError("ERROR!!! Unknown reason to cause the length of pairIndex >2 .")
                
            # < 2
            else:
                noneEmptyIdx= [ (True if ( not pairIndex[0][v] is None ) and len(pairIndex[0][v]) != 0 else False) for v in range(0,len(pairIndex[0]),1) ]
                #print("noneEmptyIdx=")
                #self.Print_Info(s=noneEmptyIdx, print_each_elem=False)
                
                noneEmptyIdxTrueCount=[True for v in noneEmptyIdx if v == True]
                #print("noneEmptyIdxTrueCount=")
                #self.Print_Info(s=noneEmptyIdxTrueCount, print_each_elem=False)
                
                noneEmptyIdxTrueCount_len=len(noneEmptyIdxTrueCount)
                
                # = 0
                if noneEmptyIdxTrueCount_len == 0 :
                    raise ValueError("ERROR!!! It refers pairIndex contains all elements as empty list. Unknown reason to cause the length of noneEmptyIdxTrueCount = 0 .")
                    
                # = 2 
                if noneEmptyIdxTrueCount_len == 2 :
                    li2=[list(map(itemgetter(0), v)) for v in pairIndex]    
                    
                    for li3 in pairIndex[0]:      
                        #print("li3=")
                        #self.Print_Info(s=li3, print_each_elem=False)
                        if len(li3)%2 !=0:
                            return False,1
                    
                    return True,2
                
                # = 1
                else:
                    for idx in range(0,len(noneEmptyIdx),1):
                        
                        #self.Print_Info(s=noneEmptyIdx[idx], print_each_elem=False)
                        if noneEmptyIdx[idx] == True:
                            numOfCnt=len(pairIndex[0][idx])
                            #print("numOfCnt=")
                            #self.Print_Info(s=numOfCnt, print_each_elem=False)
                            if numOfCnt % 2 != 0:
                                return False,3
                            
                    return True,4
                
           # = 2
        else:
            li2=[list(map(itemgetter(0), v)) for v in pairIndex]    
            if len(li2)==0:
                return True,5
            else:
                return False,6
    
    def CheckValidStringByPairIndex_ForQuote(self,s:str,pairIndex:list,options:list):
        result=self.CheckNoBracket(pairIndex,options)
        
        ok=result[0]
        errno=result[1]
        
        if options[0] == True:
            print("In the method CheckValidStringByPairIndex_ForQuote,")
            print("ok=")
            self.Print_Info(s=ok, print_each_elem=False)
            print("errno=")
            self.Print_Info(s=errno, print_each_elem=False)
            
        if ok == True:
            return None
        else:
            raise ValueError("ERROR!!! There are errors in the method CheckValidStringByPairIndex_ForQuote.")
        
    def CheckValidStringByPairIndex_ForParen(self,s:str,pairIndex:list,options:list):
        
        inst=ParenthesisProblem()
        result=inst.IsBetweenLine_WithTupleList(pairIndex,to_consider_same_parenthesis=True)
        self.Print_Info(result,print_each_elem=False)
        
        if result==True:
            raise ValueError("CheckValidStringByPairIndex") 
    
    def UnpackString(self,s:str):
         
         s=self.StripExtraSpaceAndQuote(s)     
         (s,bracketIdx)=self.StripBracket(s)
        
         self.Print_Info(s,print_each_elem=False)
         
         pairQuoteIndex=self.SplitAllQuote_String2List(s)
         
         self.CheckValidStringByPairIndex_ForQuote(s,pairQuoteIndex,[False])
         
         #self.Print_Info(pairQuoteIndex,print_each_elem=True)
         
         pairParenthesisIndex=self.SplitAllBrackets_String2List(s)
         self.Print_Info(pairParenthesisIndex,print_each_elem=False)
         
         self.CheckValidStringByPairIndex_ForParen(s,pairParenthesisIndex,[False])
         
         
         
         return None   
         
if __name__=='__main__':
    
    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"[{\'1\',\'2\',\'3\',\'4\'}]\"" \' '
    
    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"[\'1\',\'2\',\'3\',\'4\']\"" \' '

    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"{[\'1\',\'2\',\'3\',\'4\']}\"" \' '

    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"[{\'1\',[\'2\'],\'3\',\'4\'}]\"" \' '

    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"[{\'1\',{\'2\' : \'a\'},\'3\',\'4\'}]\"" \' '

    # At present, have exceptions occur.
    # ok
    #o=' \' "\"{\'1\',{\'2\' : \'a\'},\'3\',\'4\'}]\"" \' '
    
    
    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"[\'1\',{\'2\' : \'a\'},\'3\',\'4\']\"" \' '
    
    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"{\'1\',{\'2\' : \'a\'},\'3\',\'4\'}\"" \' '
    
    # At present, have exceptions occur.
    # ok
    #o=' \' "\"{\'1\',[\'2\' : \'a\'},\'3\',\'4\'}]\"" \' '
    
    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"[ {\'1\',[\'2\' : \'a\'}],\'3\',\'4\' ] \"" \' '
    
    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"[ \'1\',{ [\'2\' : \'a\'}],\'3\',\'4\' ] \"" \' '
    
    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"[ \'1\', [ {\'2\' : \'a\'}],\'3\',\'4\' ] \"" \' '
    
    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"[ \'1\', [ {\'2\' , \'a\'}],\'3\',\'4\' ] \"" \' '
    
    # At present, NO exceptions occur.
    # ok
    #o=' \' "\"[ \'1\', [ {\'2\' , \'a\'}],\'3\',\'4\', [ \' 5 \' , \' 6\'  ] ] \"" \' '
    
    # At present, have exceptions occur.
    # ok
    #o=' \'  "\"[\'1\',\'2\',\'3\',\'4\']\"" ] \' ] '
    
    # At present, have exceptions occur.
    # ok
    #o=' \'  [ [ "\"[\'1\',\'2\',\'3\',\'4\']\"" ]  ] '
    
    # At present, NO exceptions occur.
    # ok
    #o=' \'  [ [ "\"[\'1\',\'2\',\'3\',\'4\']\"" ] \' ] '
    
    s=String2AnyType()
    s.SetString(o)
    s.UnpackString(s.string)


