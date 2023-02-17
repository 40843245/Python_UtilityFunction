import os
import stat
import PySimpleGUI as sg 

from _FileProperty_class import _FileProperty
from  DirectoryOperation_class import DirectoryOperation

class FolderOperator(DirectoryOperation):
    def __init__(self
                 ,src_folderfilepath:str
                 ,need_check_filepathname_exists
                 ,need_prehandling_filepathname
                 ):
        self.src_file=_FileProperty(filepathname=src_folderfilepath
                               ,need_check_filepathname_exists=need_check_filepathname_exists
                               ,need_prehandling_filepathname=need_prehandling_filepathname
                               )
    

    def SetFilepathname(self,filepathname:str):
        self.src_file.SetFilepathname(filepathname)
        
    @staticmethod
    def GetMaxSize_ForAllSubfiles(src_folderfilepath:str):
        size = 0
        max_size = 0
        max_file =""
        hasNone=True
        hasException_origin=False
        src_folderfilepath = os.path.abspath(src_folderfilepath)
        try:
            for folder, subfolders, files in os.walk(src_folderfilepath):
                hasNone=False
                for file in files:
                    f=os.stat(os.path.join( folder, file ))
                    size=f.st_size
                    if size>max_size:
                        max_size = size
                        max_file = os.path.join( folder, file )
        except:
            hasException_origin=True
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): GetMaxSize_ForAllSubfiles"
                           ,"ERROR!!! unknown error occured while searching all files and folders.")
        result=(max_file,max_size,hasNone,hasException_origin)
        return result
    
    @staticmethod
    def GetAllFoldersAndFiles_InThisLevel(src_folderfilepath:str):
        
        hasException=False
        try:
            src_folderfilepath=os.path.abspath(src_folderfilepath)
        except TypeError:
            hasException=True
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): GetAllFoldersAndFiles_InThisLevel"
                           ,"[WinError 183] It got an unexpected keyword argument.")
            
        try:
            result=os.listdir(src_folderfilepath)
        except FileNotFoundError:
            hasException=True
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): MoveFile"
                           ,"[WinError 183] The file or directory is NOT found.")
        return result,hasException
    
    @staticmethod
    def PrintAllFoldersAndFiles_InThisLevel(src_folderfilepath:str):
        src_folderfilepath=os.path.abspath(src_folderfilepath)
        entries,hasException=FolderOperator.GetAllFoldersAndFiles_InThisLevel(src_folderfilepath=src_folderfilepath)
        hasException_origin=hasException
        if hasException:
            hasException=False
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): PrintAllFoldersAndFiles_InThisLevel"
                           ,"Skip the execution of PrintAllFoldersAndFiles_InThisLevel\n \
                               since there are exceptions on GetAllFoldersAndFiles_InThisLevel")
        else:
            hasNone=True
            for entry in entries:
                hasNone=False
                print(entry)
            return hasNone,hasException_origin
        
    @staticmethod    
    def PrintAllFolders_InThisLevel(src_folderfilepath:str):
        src_folderfilepath=os.path.abspath(src_folderfilepath)
        entries,hasException=FolderOperator.GetAllFoldersAndFiles_InThisLevel(src_folderfilepath=src_folderfilepath)
        hasException_origin=hasException
        if hasException:
            hasException=False
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): PrintAllFoldersAndFiles_InThisLevel"
                           ,"Skip the execution of PrintAllFolders_InThisLevel\n \
                               since there are exceptions on GetAllFoldersAndFiles_InThisLevel")
        else:        
            hasNone=True
            for entry in entries:
                if os.path.isdir(os.path.join(src_folderfilepath, entry)):
                    hasNone=False
                    print(entry)
            return hasNone,hasException_origin
    @staticmethod
    def PrintAllFiles_InThisLevel(src_folderfilepath:str):
        src_folderfilepath=os.path.abspath(src_folderfilepath)
        entries,hasException=FolderOperator.GetAllFoldersAndFiles_InThisLevel(src_folderfilepath=src_folderfilepath)
        hasException_origin=hasException
        if hasException:
            hasException=False
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): PrintAllFoldersAndFiles_InThisLevel"
                           ,"Skip the execution of PrintAllFiles_InThisLevel\n \
                               since there are exceptions on GetAllFoldersAndFiles_InThisLevel")
        else:        
            hasNone=True
            for entry in entries:
                if os.path.isfile(os.path.join(src_folderfilepath, entry)):
                    hasNone=False
                    print(entry)      
            return hasNone,hasException_origin
    @staticmethod
    def GetFolderStatus(src_folderfilepath:str):
        src_folderfilepath=os.path.abspath(src_folderfilepath)
        entries=os.scandir(src_folderfilepath)
        return entries
    
    @staticmethod
    def PrintFolderStatus(src_folderfilepath:str,only_print_first:bool):
        src_folderfilepath=os.path.abspath(src_folderfilepath)
        entries=FolderOperator.GetFolderStatus(src_folderfilepath)
        hasNone=True
        hasException_origin=False
        try:
            for entry in entries:
                hasNone=False
                print("--------------1------------------")
                print(entry)
                print("--------------2------------------")
                print(type(entry))
                print("--------------3------------------")
                print(dir(entry))
                print("--------------4------------------")
                print(entry.name)
                print("--------------5------------------")
                print(entry.is_file)
                print("--------------6------------------")
                print(entry.inode())
                print("--------------7------------------")
                print(entry.path)
                print("--------------8------------------")
                print(entry.is_symlink())
                print("--------------9------------------")
                print(entry.stat())
                print("--------------10------------------")
                if only_print_first:
                    break
        except:
            hasException_origin=True
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): GetMaxSize_ForAllSubfiles"
                           ,"ERROR!!! unknown error occured while printing the status of all files and folders.")
            
        return hasNone,hasException_origin
            
            
def test():
    src_folderfilepath=r"C:\Users\user\Desktop\Demo_Test"
    inst=FolderOperator(src_folderfilepath=src_folderfilepath
                      ,need_check_filepathname_exists=True                      
                      ,need_prehandling_filepathname=True)
    
    print(inst.src_file.filepathname)
    (max_file,max_size)=FolderOperator.GetMaxSize_ForAllSubfiles(path=inst.src_file.filepathname)
    print("The largest file is: "+max_file)
    print('Size: '+str(max_size)+' bytes')
    
    entries=FolderOperator.GetFolderStatus(inst.src_file.filepathname)
    FolderOperator.PrintFolderStatus(src_folderfilepath=inst.src_file.filepathname, only_print_first=False)
    
if __name__=='__main__':
    test()    
