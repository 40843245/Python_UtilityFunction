import webbrowser
from YTChannelID_class import YT_Channel_ID


class YTLinkOpener(YT_Channel_ID):
    def __init__(self,channel_ID_link):
        super().__init__(channel_ID_link)
    
    def OpenLink(self,link):
        if isinstance(link,(str)):
            webbrowser.open(str(link))
        elif isinstance(link,(tuple,list,set)):
            for v in link:
                self.OpenLink(v)
        
        else:
            raise TypeError("ERROR!!! Invalid Type!!!")
        
    def OpenYTLink(self,link):
        self.OpenLink(self.GetPlaylistsUrl())
        self.OpenLink(self.GetFeatureChannelsUrl())
        self.OpenLink(self.GetCommunityUrl())
        self.OpenLink(self.GetAboutUrl())
        self.OpenLink(self.GetAllYTUrl())
        
    
