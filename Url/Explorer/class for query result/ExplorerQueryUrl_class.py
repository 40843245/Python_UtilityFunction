from ExplorerUrl_ENUM_class import ExplorerUrl_ENUM

class ExplorerQueryUrl():
    
    Seperator="/"
    
    SearchBaseUrl="search?q="
    
    ExplorerQueryMicrosoftEdgeBaseUrl=ExplorerUrl_ENUM.ExplorerMicrosoftEdgeBaseUrl+Seperator+SearchBaseUrl
    
    ExplorerQueryGoogleBaseUrl=ExplorerUrl_ENUM.ExplorerGoogleBaseUrl+Seperator+SearchBaseUrl
    
    GOOGLE_CHROME="Google Chrome"
    
    MICROSOFT_EDGE="Microsoft Edge"
    
    def __init__(self):
        print(ExplorerQueryUrl.Seperator)
        print(ExplorerQueryUrl.SearchBaseUrl)
        print(ExplorerQueryUrl.ExplorerQueryGoogleBaseUrl)
        print(ExplorerQueryUrl.ExplorerQueryMicrosoftEdgeBaseUrl)
        self.searchUrl=""
        self.engine=ExplorerQueryUrl.GOOGLE_CHROME
    
    @staticmethod
    def GetAllAvailableEngines():
        li=[ 
            ExplorerQueryUrl.GOOGLE_CHROME
            ,ExplorerQueryUrl.MICROSOFT_EDGE
            ]
        return li
    
    def SetEngine(self,engine):
        if engine is None:
            raise TypeError
            
        if not engine in ExplorerQueryUrl.GetAllAvailableEngines():
            raise ValueError
        
        self.engine=engine
        
    def SetSearchUrl(self,query:str):
        if self.engine == ExplorerQueryUrl.GOOGLE_CHROME:
            self.searchUrl = ExplorerQueryUrl.ExplorerQueryGoogleBaseUrl+query
        elif self.engine ==  ExplorerQueryUrl.MICROSOFT_EDGE:
            self.searchUrl = ExplorerQueryUrl.ExplorerQueryMicrosoftEdgeBaseUrl + query
        
    def GetSearchUrl(self)->str:
        return self.searchUrl
        
    
def test():
    inst=ExplorerQueryUrl()
    inst.SetEngine(ExplorerQueryUrl.MICROSOFT_EDGE)
    inst.SetSearchUrl(query="result")
    
    import webbrowser
    
    webbrowser.open(inst.GetSearchUrl())
    
if __name__=='__main__':
    test()
    