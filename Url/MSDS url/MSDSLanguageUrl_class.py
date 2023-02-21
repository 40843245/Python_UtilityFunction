class MSDSLanguageUrl():
    Seperator="/"
    MSDSLanguageBaseUrl="https://learn.microsoft.com"
    
    def __init__(self):
        self.query=""
        self.queryUrl=""
        
    @staticmethod
    def MSDSLanguageUrlQuery(query:str,la="en-us"):
        result=MSDSLanguageUrl.MSDSLanguageBaseUrl+MSDSLanguageUrl.Seperator+la+MSDSLanguageUrl.Seperator
        return result
    def MSDSLanguageUrlQuery_Self(self,la="en-us"):
        self.queryUrl=MSDSLanguageUrl.MSDSLanguageUrlQuery(query=self.query,la=la)
        return self.queryUrl
    def SetQuery(self,query):
        self.query=query
    
        
    
def test():
    r="aspnet/web-api/overview/web-api-routing-and-actions/routing-in-aspnet-web-api"
    inst=MSDSLanguageUrl()
    inst.SetQuery(query=r)
    #result=inst.MSDSLanguageUrlQuery_Self(la="en-us")
    result=MSDSLanguageUrl.MSDSLanguageUrlQuery(r)
    import webbrowser
    webbrowser.open(result)
if __name__=='__main__':
    test()