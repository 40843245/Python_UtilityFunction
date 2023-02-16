from operator import itemgetter

from Message_ENUM_class import Message_Enum
from Type_ENUM_class import Type_Enum
from Bracket_ENUM_class import Bracket_ENUM
    
    
class ParenthesisProblem():
    
    def IsParenthesisMatched(self,s1:str,s2:str)->bool:     
        st=s1+s2
        pair_s=[ (''.join(Bracket_ENUM.pair[i])) for i in range(0,len(Bracket_ENUM.pair),1)]
        #print(pair_s)
        #print(st)
        pair_set=set(pair_s)
        st_set=set(st)
        
        for p_set in pair_set:
            intersection_set=st_set.intersection(p_set)
            #print(intersection_set)
            if len(st_set)==len(intersection_set):
                return True
            
        return False
        
    def sort_key1(self,val):
        return val[0]
       
    def IsBetweenLine_WithList(self,li:list)->bool:
        
        if li is None:
            return False
        
        if len(li)==0:
            return False
        
        li.sort(key=self.sort_key1, reverse=False)
        for idx in range(0,len(li),1):
            li_idx=li[idx]
            for jdx in range(idx+1,len(li),1):
                li_jdx=li[jdx]
                if (li_jdx[1]-li_idx[1])*(li_jdx[0]-li_idx[0])*(li_jdx[0]-li_idx[1])<0:
                    return True,idx,jdx,li_idx,li_jdx
        return False,-1,-1,[],[]
    
    # To handle the type such as [(1,1),(2,2)]
    def IsBetweenLine_WithTupleList(self,li:list,to_consider_same_parenthesis:bool)->bool:
          
        if to_consider_same_parenthesis == False:
            li2=[list(map(itemgetter(0), v)) for v in li]
            print(li2)
            result=self.IsBetweenLine_WithList(li2)
            return result[0]
        else:
            
            if li is None:
                return False
            
            if len(li)==0:
                return False
            
            li.sort(key=self.sort_key1, reverse=False)
            for idx in range(0,len(li),1):
                li_idx=li[idx]
                for jdx in range(idx+1,len(li),1):
                    li_jdx=li[jdx]
                    if (li_jdx[1][0]-li_idx[1][0])*(li_jdx[0][0]-li_idx[0][0])*(li_jdx[0][0]-li_idx[1][0])<0:
                        if self.IsParenthesisMatched(s1=li_jdx[0][1], s2=li_idx[1][1]):
                            return True
                        
            return False
            

    def main(self):
        for cnt in range(0,1,1):
            list1=[[6, 19], [30, 46], [8, 18]]
            
            result,idx,jdx,li_idx,li_jdx=self.IsBetweenLine_WithList(list1)
    
            print("start of ------------------------------------------ no."+str(cnt))
    
            print(list1)
            print(result)
            print(idx)
            print(jdx)
            print(li_idx)
            print(li_jdx)

            print("end of ------------------------------------------ no."+str(cnt))

if __name__=='__main__':
    inst=ParenthesisProblem()
    inst.main()