import os 
import sys

from PathDirectory_ENUM_class import PathDirectory_ENUM, PathDirectory

class _FileProperty():
    def __dict__(self):
        keys_li=[
            "need_check_filepathname_exists:"
            ,"need_prehandling_filepahname:"
            ,"pathDir:"
            ,"isFile:"
            ,"isDir:"
            ,"isSymbolicLink:"
            ,"isMount:"
            ,"filesize:"
            ,"absPath:"
            ,"relPath:"
            ,"realPath:"
            ,"normalPath:"
            ,"normalCase:"
            ,"dirName:"
            ,"fileExt:"
            ,"fileDrive:"
            ,"filepathname_withoutExt:"
            ,"filepathname_withoutDrive:"
            ,"curPlatform:"
        ]
        
        values_li=self.__list__()
        
        dic={}
        for idx in range(0,len(keys_li),1):
            dic.update({keys_li[idx]:values_li[idx]})
        return dic
    
    def __list__(self):
        li=[
        self.need_check_filepathname_exists
        ,self.need_prehandling_filepahname
        ,self.pathDir
        ,self.isFile
        ,self.isDir
        ,self.isSymbolicLink
        ,self.isMount
        ,self.filesize
        ,self.absPath
        ,self.relPath
        ,self.realPath
        ,self.normalPath
        ,self.normalCase
        ,self.dirName
        ,self.fileExt
        ,self.fileDrive
        ,self.filepathname_withoutExt
        ,self.filepathname_withoutDrive
        ,self.curPlatform
        ]
        return li 
    
    def __init__(self
                 ,filepathname:str
                 ,need_check_filepathname_exists:bool
                 ,need_prehandling_filepathname:bool):
        
        self.need_check_filepathname_exists=need_check_filepathname_exists
        self.need_prehandling_filepathname=need_prehandling_filepathname
       
        self.filepathname=filepathname
        argv=[None for _ in range(0,self.ARGC(),1)]
        index=0
        self.pathDir=argv[index]
        index+=1
        self.isFile=argv[index]
        index+=1
        self.isDir=argv[index]
        index+=1
        self.isSymbolicLink=argv[index]
        index+=1
        self.isMount=argv[index]
        index+=1
        self.filesize=argv[index]
        index+=1
        self.absPath=argv[index]
        index+=1
        self.relPath=argv[index]
        index+=1
        self.realPath=argv[index]
        index+=1
        self.normalPath=argv[index]
        index+=1
        self.normalCase=argv[index]
        index+=1
        self.dirName=argv[index]
        index+=1
        self.fileExt=argv[index]
        index+=1
        self.fileDrive=argv[index]
        index+=1
        self.filepathname_withoutExt=argv[index]
        index+=1
        self.filepathname_withoutDrive=argv[index]

        self.curPlatform=sys.platform
        self.pathDir=self.GetSystemRootDirectory()
    
        if need_check_filepathname_exists:
            self.CheckFileExists(self.filepathname)
        if need_prehandling_filepathname:
            result=self.PreHandlingFilePathName(self.filepathname)
            self.UpdateValues(*result)
    
    @staticmethod
    def ARGC():
        return 16
    
    def SetFilepathname(self,filepathname:str):
        self.filepathname=filepathname
        
    # *argv: Non-Keyword Arguments
    def UpdateValues(self,*argv):
        
        argc=self.ARGC()
        if len(argv)<argc:
            raise ValueError("ERROR!!! To less parameters passed to update the attributes of the class!!!")
        elif len(argv)>argc:
            raise ValueError("ERROR!!! To more parameters passed to update the attributes of the class!!!")
            
        index=0
        self.pathDir=argv[index]
        index+=1
        self.isFile=argv[index]
        index+=1
        self.isDir=argv[index]
        index+=1
        self.isSymbolicLink=argv[index]
        index+=1
        self.isMount=argv[index]
        index+=1
        self.filesize=argv[index]
        index+=1
        self.absPath=argv[index]
        index+=1
        self.relPath=argv[index]
        index+=1
        self.realPath=argv[index]
        index+=1
        self.normalPath=argv[index]
        index+=1
        self.normalCase=argv[index]
        index+=1
        self.dirName=argv[index]
        index+=1
        self.fileExt=argv[index]
        index+=1
        self.fileDrive=argv[index]
        index+=1
        self.filepathname_withoutExt=argv[index]
        index+=1
        self.filepathname_withoutDrive=argv[index]
              
    def GetSystemRootDirectory(self):
        currPlatfrom=sys.platform
        currpathDir=PathDirectory.GetPathDirectory(currSystem=currPlatfrom)
        if currpathDir is None:
            raise Exception("EXCEPTION!!! The directory for path of currently used platform is None!!!")
        return currpathDir
    
    def CheckFileExists(self,filepathname:str):
        if os.path.exists(filepathname):
            Exception("EXCEPTION!!! The filepathname does NOT exist. Check the spelling!!!")
    
            
    def PreHandlingFilePathName(self,filepathname:str):
        
        pathDir=self.GetSystemRootDirectory()
        
        isFile=os.path.isfile(path=filepathname)
        
        isDir=os.path.isdir(filepathname)
        
        isSymbolicLink=os.path.islink(path=filepathname)
        
        isMount=os.path.ismount(path=filepathname)
        
        fileSize=os.path.getsize(filepathname)
        
        absPath=os.path.abspath(path=filepathname)
        
        relPath=os.path.relpath(path=filepathname, start=os.curdir)
        
        normalPath=os.path.normpath(filepathname)
        
        normalCase=os.path.normcase(filepathname)
        
        realPath=os.path.realpath(path=filepathname)
        
        dirName=os.path.dirname(filepathname)
        
        filepathname_withoutExt,fileExt=os.path.splitext(filepathname)
        
        fileDrive,filepathname_withoutDrive=os.path.splitdrive(filepathname)
        
        filepathname_withoutDrive=filepathname_withoutDrive.lstrip(pathDir)
        
        
        result=(
                pathDir
                ,isFile
                ,isDir
                ,isSymbolicLink
                ,isMount
                ,fileSize
                ,absPath
                ,relPath
                ,realPath
                ,normalPath
                ,normalCase
                ,dirName
                ,fileExt
                ,fileDrive
                ,filepathname_withoutExt
                ,filepathname_withoutDrive
                )
        return result
        

def test():
    filepathname=r'C:\Users\user\Desktop'
    inst=_FileProperty(filepathname=filepathname
                       ,need_check_filepathname_exists=True
                       ,need_prehandling_filepahname=True)
    result=inst.__list__()
    for x in result:
        print(x)
        
    result=inst.__dict__()
    print(result)
    
    
if __name__=='__main__':
    test()
        
        
        
