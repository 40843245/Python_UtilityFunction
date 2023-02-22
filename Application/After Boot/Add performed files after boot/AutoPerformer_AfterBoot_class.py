from FileOperator_class import FileOperator

class AutoPerformer_AfterBoot(FileOperator):
    
    STARTUP_LOC=r"C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    def  __init__(self
                 ,src_filepathname:str
                 #,dest_filepathname:str
                 ,need_check_filepathname_exists
                 ,need_prehandling_filepathname
                 ):
        dest_filepathname=AutoPerformer_AfterBoot.STARTUP_LOC
        super().__init__(src_filepathname=src_filepathname
                         ,dest_filepathname=dest_filepathname
                         ,need_check_filepathname_exists=need_check_filepathname_exists
                         ,need_prehandling_filepathname=need_prehandling_filepathname
                         )
        
    def AddAutoOpenedApp(self):
        self.Copy()
    
def test():
    #filepathname=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Access.lnk"
    filepathname=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
    inst=AutoPerformer_AfterBoot(src_filepathname=filepathname
                                 ,need_check_filepathname_exists=[False,False]
                                 ,need_prehandling_filepathname=[False,False]
                                 )
    #inst.AddAutoOpenedApp()
    #filepathname=r"C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Word.lnk"
    #inst.SetSrcFilepathname(src_filepathname=filepathname
              #              , need_check_filepathname_exists=False
               #             , need_prehandling_filepathname=False)
    #inst.RemoveSrcFile()
    filepathname=r"C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    inst.SetSrcFilepathname(src_filepathname=filepathname
                            , need_check_filepathname_exists=False
                            , need_prehandling_filepathname=False)
    result=inst.src_file.filepathname
    print(result)
    inst.ClearAllFilesInSameDirectoryOfSrcFile()
    
    
if __name__=='__main__':
    test()