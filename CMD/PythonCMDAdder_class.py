import sys

from LetterHandler_class import LetterHandler

class PythonCMDAdder():
    
    @staticmethod
    def PythonCMD_InPythonShell(s:str):
        d="\n"
        s2=">>> "
        tf=True
        result=LetterHandler.InsertAtBegin_AtMultiLine(s1=s
                                                ,delim=d
                                                ,s2=s2
                                                ,need_to_strip_extra_atbegin_after_join=tf)
        return result
    
    @staticmethod
    def PythonCMD_InDOS(s:str,need_merge_lines:bool,is_in_anaconda_spyder:bool):
        version= sys.version
        Python_version = version.split(".")  
        word = None
        
        if is_in_anaconda_spyder:
            word="python"
        elif int(Python_version[0]) >=4:
            word="python3"
        elif int(Python_version[0]) == 3:
            if int(Python_version[1])>=2:
                word="python3"
            else:
                word="python"
        else:
            word="python"
        result = word + " " + s 
        if need_merge_lines:
            result=result.replace("\n"," ")
        return result
            
def test():
    
    s="1\n2\n3\n4"
    result=PythonCMDAdder.PythonCMD_InDOS(s=s,need_merge_lines=True)
    print(result)
    
if __name__=='__main__':
    test()
        
        
        

