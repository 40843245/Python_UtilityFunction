import json 
from Letter_ENUM_class import Letter_ENUM
from Data_class import Data

class DataToString():
    def __init__(self):
        self.data=None
        self.string=None
        
        
    def SetData(self,data):
        self.data=data
    
    def ToString(self
                 ,to_be_list_like:bool
                 ,to_be_dict_like:bool
                 ,to_be_set_like:bool
                 ,to_be_tuple_like:bool
                 ,need_bracket:bool
                 ,bracketOption:Letter_ENUM
                 ,do_recusive:bool
                 ,join_letter:str)->str:
        
        
        
        if self.data is None:
            self.string="None"
            return "None"
        
        if isinstance(self.data,(str)):
            self.string=self.data
            return self.data
        
        if isinstance(self.data,(int,bool)):
            self.string=str(self.data)
            
            if need_bracket:
                self.string=bracketOption+self.string+bracketOption
                
            return str(self.data)
        
        if isinstance(self.data,(dict)):
            if to_be_dict_like:
                self.string=json.dumps(self.data)
                
                if need_bracket:
                    self.string=bracketOption+self.string+bracketOption
                    
                return self.string
            else:
                if do_recusive:
                    da=Data
                    li=da.GetNestedDatas(self.data)
                    if to_be_list_like:
                        join_letter=Letter_ENUM.comma
                        x=join_letter.join(self.data)
                        self.string=Letter_ENUM.leftSquareBracket+x+Letter_ENUM.rightSquareBracket
                    else:
                        self.string=join_letter.join(self.data)
                        
                    if need_bracket:
                        self.string=bracketOption+self.string+bracketOption
                        
                    return self.string
                else:
                    raise TypeError
                

        if isinstance(self.data,(list)):
            if to_be_list_like:
                join_letter=Letter_ENUM.comma
                x=join_letter.join(self.data)
                self.string=Letter_ENUM.leftSquareBracket+x+Letter_ENUM.rightSquareBracket
            else:
                self.string=join_letter.join(self.data)
                
            if need_bracket:
                self.string=bracketOption+self.string+bracketOption
                
            return self.string
        
        if isinstance(self.data,(set)):
            if to_be_set_like:
                join_letter=Letter_ENUM.comma
                x=join_letter.join(self.data)
                self.string=Letter_ENUM.leftCurlyBracket+x+Letter_ENUM.rightCurlyBracket
            else:
                self.string=join_letter.join(self.data)
                
            if need_bracket:
                self.string=bracketOption+self.string+bracketOption
            
            return self.string
        
        if isinstance(self.data,(tuple)):
            if to_be_tuple_like:
                join_letter=Letter_ENUM.comma
                x=join_letter.join(self.data)
                self.string=Letter_ENUM.leftParentheses+x+Letter_ENUM.rightParentheses
            else:
                self.string=join_letter.join(self.data)
                
            if need_bracket:
                self.string=bracketOption+self.string+bracketOption
                
            return self.string
        
        
        
if __name__=='__main__':
    o=["a","b","c"]
    D2S=DataToString()
    D2S.SetData(o)
    result=D2S.ToString(to_be_list_like=True
                        , to_be_dict_like=False
                        , to_be_set_like=False
                        , to_be_tuple_like=False
                        , need_bracket=True
                        , bracketOption = Letter_ENUM.singleQuote
                        , do_recusive=False
                        , join_letter=Letter_ENUM.whitespace)
    print(result)
    print(type(result))
