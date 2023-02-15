import os
import json

from Letter_ENUM_class import Letter_ENUM
class WriteStream():

    def __init__(self):
        self.filepath=Letter_ENUM.emptyString
        self.filepathname=Letter_ENUM.emptyString
        self.fileExt=Letter_ENUM.emptyString
        self.file=None
        self.textContent=None
    
    def SetPath(self,filepath,filename,fileExt):
        self.filename=filename
        self.fileExt=fileExt
        self.filepath=filepath
        
        self.filepath=self.filepath.rstrip(Letter_ENUM.whitespace).rstrip(Letter_ENUM.tab).rstrip(Letter_ENUM.newline)
        self.filepathname=os.path.join(self.filepath,self.filename)                
        self.filepathname=self.filepathname.replace("/","\\")+fileExt
        
    def WriteData(self,textContent):
        self.file=open(self.filepathname,"w")
        self.textContent=textContent
        if isinstance(self.textContent,(str,int,bool)):
            self.file.write(str(self.textContent))
        elif isinstance(self.textContent,(dict)):       
            self.file.write(str(json.dumps(self.textContent)))
        elif isinstance(self.textContent,(tuple,list,set)):
            self.file.write(str(self.textContent))
        self.file.close()
