from PIL import ImageGrab
import time

class Screenshot():
    
    @staticmethod
    def TakeAScreenshot(filepathname,ext):
        ImageGrab.grab().save(filepathname, ext)
        
    @staticmethod
    def TakeAScreenshot_afterSecond(sec:int,filepathname,ext):
        if sec<=0:
            raise ValueError("ERROR!!! second must be > = 1")
        time.sleep(sec)
        Screenshot.TakeAScreenshot()
    
    @staticmethod 
    def TakeManyScreenshots_afterSecond(start_sec:int
                                        ,interval_sec:int
                                        ,repeat_times:int
                                        ,filepathname
                                        ,ext):
        if start_sec<=0:
            raise ValueError("ERROR!!! second must be > = 1")
        
        if interval_sec<=0:
            raise ValueError("ERROR!!! second must be > = 1")
            
        if repeat_times<=0:
            raise ValueError("ERROR!!! second must be > = 1")
            
        Screenshot.TakeAScreenshot_afterSecond(sec=start_sec,filepathname=filepathname,ext=ext)
        
        for idx in range(1,repeat_times,1):
            Screenshot.TakeAScreenshot_afterSecond(sec=interval_sec,filepathname=filepathname,ext=ext)
            
    
