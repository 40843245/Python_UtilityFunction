class Data():
    
    def __init__(self): 
        self.NOTFOUND=-1
        self.result=[]  
        
    def GetNestedDatas(self,data):
        self.GetNestedData(data)
        return self.result
            
    def GetNestedData(self,data): 
        if data is None:
            return None     
        if isinstance(data,(str,int,bool)):
            self.result.append(data)
            return None
        if isinstance(data,(tuple,set,list)):
            for v in data:
                self.GetNestedData(v)
                return None
        if isinstance(data,(dict)):
            for k,v in data.items():
                if len(k)==1:
                    self.result.append(k)
                else:
                    self.GetNestedData(k)          
                if isinstance(v,(list,tuple,set,dict)) or len(v)==1:
                    self.result.append(v)       
                else:
                    self.GetNestedData(v)
        return None
    
    def GetValueByKeyInNestedDatas(self,data,key,containValue:bool):
        if isinstance(data,(str,int,bool)):
            if data==key:
                if containValue==True:
                    return key
                else:
                    return self.NOTFOUND
            else:
                return self.NOTFOUND
        if isinstance(data,(set,tuple,list)):
            for v in data:
                result=self.GetValueByKeyInNestedDatas(v,key,containValue=containValue)
                if result!=self.NOTFOUND:
                    return result
            return self.NOTFOUND
        if isinstance(data,(dict)):
            if key in data.keys():
                return data[key]
            else:
                for k,v in data.items():
                    result=self.GetValueByKeyInNestedDatas(v,key,containValue=containValue)
                    if result!=self.NOTFOUND:
                        return result
                return self.NOTFOUND
