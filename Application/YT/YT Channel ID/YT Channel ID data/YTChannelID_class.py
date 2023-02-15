import pytube
from pytube import YouTube

from Data_class import Data
from Letter_ENUM_class import Letter_ENUM

class YT_Channel_ID(Data):
    def __init__(self,channel_ID_link):
        super().__init__()
             
        self.channel_ID_link=channel_ID_link
        self.channel=self.GetChannelByChannelID()
        
        self.channel_id=self.GetChannelID()
        self.channel_all_video_urls=self.GetAllYTUrl()
        self.channel_playlists_urls=self.GetPlaylistsUrl()
        self.channel_name=self.GetYTChannelName()
        self.featured_channels_url=self.GetFeatureChannelsUrl()
        self.community_url=self.GetCommunityUrl()
        self.about_url=self.GetAboutUrl()
        self.yt_api_key=self.GetYTAPIKey()
        
        self.initial_data=self.GetInitialData()
        
    def GetChannelByChannelID(self):
        return pytube.Channel(self.channel_ID_link)
    
    def GetChannelID(self):
        return self.channel.channel_id
    
    def GetPlaylistsUrl(self):
        return self.channel.playlists_url
    
    def GetAllYTUrl(self):
        return list(self.channel.video_urls)
    
    def GetYTChannelName(self):
        return self.channel.channel_name
    
    def GetFeatureChannelsUrl(self):
        return self.channel.featured_channels_url
    
    def GetCommunityUrl(self):
        return self.channel.community_url
    
    def GetAboutUrl(self):
        return self.channel.about_url
    
    def GetYTAPIKey(self):
        return self.channel.yt_api_key
    
    def GetInitialData(self):
        return self.channel.initial_data
     
    def __list__(self):
        li=[
            self.GetYTChannelName()
            ,self.GetFeatureChannelsUrl()
            ,self.GetCommunityUrl()
            ,self.GetAboutUrl()
            ,self.GetPlaylistsUrl()
            ,self.GetYTAPIKey()
            ,self.GetAllYTUrl()
        ]
        return li
    
    def GetAllKey(self):
        li=[
            "self.GetYTChannelName:"
            ,"self.GetFeatureChannelsUrl:"
            ,"self.GetCommunityUrl:"
            ,"self.GetAboutUrl:"
            ,"self.GetPlaylistsUrl:"
            ,"self.GetYTAPIKey:"
            ,"self.GetAllYTUrl:"
            
        ]
        return li
    def __dict__(self):
        v_li=self.__list__()
        k_li=self.GetAllKey()
        dic=dict()
        for j in range(0,len(v_li),1):
            k_elem=k_li[j]
            v_elem=v_li[j]
            t={k_elem:v_elem}
            dic.update(t)
        return dic
            
