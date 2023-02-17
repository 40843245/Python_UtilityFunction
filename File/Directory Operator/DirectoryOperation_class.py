import os
import stat
import shutil
import PySimpleGUI as sg
class DirectoryOperation():
    
    @staticmethod
    def MakeDirectory(path,mode=0o777,dir_fd=None):    
        try:
            os.mkdir(path,mode=mode,dir_fd=dir_fd)
        except FileExistsError:
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): MakeDirectory"
                           ,"[WinError 183] Cannot create a file when that file already exists.")
    
    @staticmethod
    def MakeDirectories(path,mode=0o666,exist_ok=False):
        try:
            os.makedirs(path,mode=mode,exist_ok=exist_ok)
        except FileExistsError:
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): MakeDirectories"
                           ,"[WinError 183] Cannot create a file when that file already exists.")
        
    
    @staticmethod
    def Delete(path,ignore_errors=False):
        try:
            shutil.rmtree(path, ignore_errors=ignore_errors)
        except FileNotFoundError:
            sg.popup_error(f"ERRROR occurs"
                           ,"traceback (from last call): Delete"
                           ,"[WinError 183] Cannot delete a file or directory that does NOT exists.")


