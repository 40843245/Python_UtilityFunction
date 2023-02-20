import os

from PythonCMDAdder_class import PythonCMDAdder

class PythonCMDRunner():
    
    @staticmethod 
    def Run_InDOS(filepathname:str):
        filepathname=PythonCMDAdder.PythonCMD_InDOS(filepathname
                                                    ,need_merge_lines=True
                                                    ,is_in_anaconda_spyder=True)
        os.system(filepathname)
    
def test():
    filepathname=r"C:\Users\user\test1.py"
    PythonCMDRunner.Run_InDOS(filepathname=filepathname)
    
if __name__=='__main__':
    test()
        
