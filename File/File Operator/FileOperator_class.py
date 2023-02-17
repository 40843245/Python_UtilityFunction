import os
import stat
import shutil
import PySimpleGUI as sg 

from _FileProperty_class import _FileProperty
from  DirectoryOperation_class import DirectoryOperation

class FileOperator(DirectoryOperation):
    def __init__(self
                 ,src_filepathname:str
                 ,dest_filepathname:str
                 ,need_check_filepathname_exists
                 ,need_prehandling_filepathname
                 ):
        
        self.CheckNestedDataType(o=need_check_filepathname_exists,tp=list,len_should_be=2)
        self.CheckNestedDataType(o=need_prehandling_filepathname,tp=list,len_should_be=2)
        
        self.src_file=_FileProperty(filepathname=src_filepathname
                               ,need_check_filepathname_exists=need_check_filepathname_exists[0]
                               ,need_prehandling_filepathname=need_prehandling_filepathname[0]
                               )
        self.dest_file=_FileProperty(filepathname=dest_filepathname
                               ,need_check_filepathname_exists=need_check_filepathname_exists[1]
                               ,need_prehandling_filepathname=need_prehandling_filepathname[1]
                               )
    
    def SetAllFilepathname(self
                           ,src_filepathname:str
                           ,dest_filepathname:str
                           ,need_check_filepathname_exists
                           ,need_prehandling_filepathname):
        self.CheckNestedDataType(o=need_check_filepathname_exists,tp=list,len_should_be=2)
        self.CheckNestedDataType(o=need_prehandling_filepathname,tp=list,len_should_be=2)
        
        self.SetSrcFilepathname(src_filepathname=src_filepathname
                                ,need_check_filepathname_exists=need_check_filepathname_exists[0]
                                ,need_prehandling_filepathname=need_prehandling_filepathname[0]
                                )
        self.SetDestFilepathname(dest_filepathname=dest_filepathname
                                ,need_check_filepathname_exists=need_check_filepathname_exists[1]
                                ,need_prehandling_filepathname=need_prehandling_filepathname[1]
                                )
        
    def SetSrcFilepathname(self
                           ,src_filepathname:str
                           ,need_check_filepathname_exists:bool
                           ,need_prehandling_filepathname:bool):
        
        self.src_file.SetFilepathname(src_filepathname)
        if need_prehandling_filepathname:
            self.src_file.PreHandlingFilePathName(self.src_file.filepathname)
        
    def SetDestFilepathname(self
                            ,dest_filepathname:str
                            ,need_check_filepathname_exists:bool
                            ,need_prehandling_filepathname:bool):
        
        self.dest_file.SetFilepathname(dest_filepathname)
        if need_prehandling_filepathname:
            self.dest_file.PreHandlingFilePathName(self.dest_file.filepathname)
        
    def CheckNestedDataType(self,o,tp,len_should_be:int):
        if not isinstance(o,(tp)):
            raise TypeError("ERROR!!! Mismatched type in CheckNestedDataType!!!")
        if len(o)!=len_should_be:
            raise ValueError("ERROR!!! The length of o should be the number len_should_be.")
        
        
    def CopyFile(self,*argv,follow_symlinks:bool):
        shutil.copyfile(self.src_file.filepathname
                        ,self.dest_file.filepathname
                        ,*argv
                        ,follow_symlinks=follow_symlinks)
        
    def MoveFile(self,*argv,follow_symlinks:bool,copy_func=shutil.copy2):     
        try:
            shutil.move(self.src_file.filepathname
                            ,self.dest_file.filepathname
                            ,copy_function=copy_func)
        except FileNotFoundError:
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): MoveFile"
                           ,"[WinError 183] Cannot delete a file or directory that does NOT exists.")
            
        except FileExistsError:
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): MoveFile"
                           ,"[WinError 183] Cannot create a file or directory that already exists.")
    
    def RemoveReadonly(self,func, path, _):
        """Clear the readonly bit and reattempt the removal"""
        os.chmod(path, stat.S_IWRITE)
        func(path)
        
    # NOT available in Windows
    def CreateArchive(self):
        archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
        root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
        shutil.make_archive(archive_name, 'gztar', root_dir)
def test():
    src_filepathname=r"C:\Users\user\Desktop\t.txt"
    dest_filepathname=r"C:\Users\user\Desktop\t2.txt"
    inst=FileOperator(src_filepathname=src_filepathname
                      ,dest_filepathname=dest_filepathname
                      ,need_check_filepathname_exists=[True,True]
                      ,need_prehandling_filepathname=[True,True])
    
    inst.CopyFile(follow_symlinks=False)
    
    
if __name__=='__main__':
    test()    
