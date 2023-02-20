
## ------------------------------------------------ ##
# Class of ADT to handle the letters.
# Special Terms.
# ADT is the abbreviation of Abstract Data Types.
## ------------------------------------------------ ##
class LetterHandler():
    
    # A method to transfrom for each lines.
    # The parameter func must be callable such as function or method of a class.
    @staticmethod
    def Transfrom_AtMultiLine(src_s1:str
                              ,need_to_strip_extra_all_after_join:bool
                              ,need_to_strip_extra_atbegin_after_join:bool
                              ,need_to_strip_extra_atend_after_join:bool
                              ,delim='\n'
                              ,func=None
                              ,src_s2=None):
        if src_s2==None:
            src_s2=src_s1
        li=src_s1.split(delim)
        argv=(src_s2)
        li2=[func(s,argv) for s in li]
        #s2=''.join(li2)
        s2=delim.join(li2)
        
        result=s2      
        if need_to_strip_extra_all_after_join:
            result= LetterHandler.RemoveAllExtraToOne(s1=result,delim=src_s2)
            
        elif need_to_strip_extra_atbegin_after_join:
            result= LetterHandler.RemoveBeginExtraToOne(s1=result,delim=src_s2)
            
        elif need_to_strip_extra_atend_after_join:
            result= LetterHandler.RemovEndExtraToOne(s1=result,delim=src_s2)  
        return result
    
    @staticmethod
    def RemoveBeginExtraToOne(s1:str,delim:str):
        needToFill = True if s1.startswith(delim) else False
        result=s1.lstrip(delim)
        if needToFill:
            result=delim + result
        return result
    
    @staticmethod
    def RemovEndExtraToOne(s1:str,delim:str):
        needToFill = True if s1.endswith(delim) else False
        result=s1.rstrip(delim)
        if needToFill:
            result = result + delim
        return result
    
    @staticmethod
    def RemoveAllExtraToOne(s1:str,delim:str):
       result = LetterHandler.RemoveBeginExtraToOne(s1,delim)
       result = LetterHandler.RemovEndExtraToOne(result,delim)
       return result
    
        
    
    @staticmethod
    def Append(s1:str,s2:str,*argv)->str:
        return s1+s2
    
    @staticmethod
    def Append_AtMultiLine(s1:str
                           ,delim:str
                           ,s2:str
                           ,need_to_strip_extra_all_after_join=False
                           ,need_to_strip_extra_atbegin_after_join=False
                           ,need_to_strip_extra_atend_after_join=False
                           ):
        
        
        result=LetterHandler.Transfrom_AtMultiLine(src_s1=s1
                                                   ,delim=delim
                                                   ,func=LetterHandler.Append
                                                   ,src_s2=s2
                                                   ,need_to_strip_extra_all_after_join=need_to_strip_extra_all_after_join
                                                   ,need_to_strip_extra_atbegin_after_join=need_to_strip_extra_atbegin_after_join
                                                   ,need_to_strip_extra_atend_after_join=need_to_strip_extra_atend_after_join
                                                   )
        return result
    
    @staticmethod
    def InsertAtBegin(s1:str,s2:str,*argv)->str:
        return s2+s1
    
    @staticmethod
    def InsertAtBegin_AtMultiLine(s1:str
                                  ,delim:str
                                  ,s2:str
                                  ,need_to_strip_extra_all_after_join=False
                                  ,need_to_strip_extra_atbegin_after_join=False
                                  ,need_to_strip_extra_atend_after_join=False
                                  ):
        result=LetterHandler.Transfrom_AtMultiLine(src_s1=s1
                                                   ,delim=delim
                                                   ,func=LetterHandler.InsertAtBegin
                                                   ,src_s2=s2
                                                   ,need_to_strip_extra_all_after_join=need_to_strip_extra_all_after_join
                                                   ,need_to_strip_extra_atbegin_after_join=need_to_strip_extra_atbegin_after_join
                                                   ,need_to_strip_extra_atend_after_join=need_to_strip_extra_atend_after_join
                                                   )
        return result
    
    
def test():
    
    """
    s1="123\n123\n\n"
    s3="123\n123"
    s2=">>>"
    """
    s1="123@123@"
    s3="123@123"
    s2=">>> "
    d='@'
    tf_list=[True]
    for tf in tf_list:
        result=LetterHandler.Append_AtMultiLine(s1=s3,delim=d,s2=s2)
        print(result)
        result=LetterHandler.Append_AtMultiLine(s1=s3,delim=d,s2=s2,need_to_strip_extra_all_after_join=tf)
        print(result)
        result=LetterHandler.InsertAtBegin_AtMultiLine(s1=s3,delim=d,s2=s2,need_to_strip_extra_atbegin_after_join=tf)
        print(result)
        result=LetterHandler.InsertAtBegin_AtMultiLine(s1=s3,delim=d,s2=s2,need_to_strip_extra_atend_after_join=tf)
        print(result)
if __name__=='__main__':
    test()
