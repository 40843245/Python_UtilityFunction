from re import compile as _Re

class Text():
    _unicode_chr_splitter = _Re( '(?s)((?:[\ud800-\udbff][\udc00-\udfff])|.)' ).split

    @staticmethod 
    def split_unicode_chrs( text ):
        return [ chr for chr in Text._unicode_chr_splitter( text ) if chr ]
        
    
    @staticmethod 
    def TextReplace(tar:str,replaced_dict:dict):
        whitespace=" "
        emptyString=""
        words=Text.split_unicode_chrs(tar)
        result=[]
        for word in words:
            if word in replaced_dict.keys():
                result.append(replaced_dict[word])
            else:
                result.append(word)
        
        result=emptyString.join(result)
        return result

        
def test():
    from DirtyWords_class import DirtyWords
    tar="I fuck you"
    tar=u"死一死算了"
    result=Text.TextReplace(tar=tar,replaced_dict=DirtyWords.dirtyWords)
    print(result)
if __name__=='__main__':
    test()