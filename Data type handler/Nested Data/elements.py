from found_macro import FoundMacro

class Elements():
    """
	Description:
    	Utility method that check the object `src` with type `object_type` is None or empty.
	Paramater:
   		src:source object.
        object_type:must be a data type.
    Returned Value:
		Return True iff `src` is None or empty for type `object_type`. Otherwise, return False.
    Example:
    	Example1:
			x = dict()
			result = Elements.is_empty_object(src=x,object_type=dict)
			print(result) # True
    """
    @staticmethod
    def is_empty_object(src,object_type):
        if src is None:
            return True
        if isinstance(src,(object_type)) == True:
            if src == object_type() or src is object_type():
                return True    
        return False

    """
	Description:
    	check an object `src` is None or empty of one of these type:str,dict,list,tuple.
	Paramater:
   		src: source object
    Returned Value:
		Return True iff `src` is None or empty of one of these type:str,dict,list,tuple (i.e. Returns True iff src == '', or src == or is one of these objects {},[],() respectively).  Otherwise, return False.
	NOTICE: 
    	1. It will invoke Elements.is_empty_object.
    """ 
    @staticmethod
    def is_empty(src) -> bool:
        if src is None:
            return True
        if src == '':
            return True
        if Elements.is_empty_object(src=src,object_type=list) == True:
            return True
        if Elements.is_empty_object(src=src,object_type=tuple) == True:
            return True
        if Elements.is_empty_object(src=src,object_type=dict) == True:
            return True
        return False

    """
	Description:
    	A recursive method that check the object `src` contains the elem `dest`.
	Paramater:
   		src: source object. It can be Any. However, the elem will be checked iff it is one of these types: list,tuple,dict.
        dest: value that we want to find.
    Returned Value:
		Return True iff `src` == `dest` or `src` contains `dest`.  Otherwise, return False.
	NOTICE: 
    	1. It may invoke the method itself. Thus, it may spend some time if the given `src` is too complicated.
    """ 
    @staticmethod
    def contains(src,dest) -> bool:
        if dest == src :
            return True
        if isinstance(src,(list,tuple,dict)) == False:
            return False
        for elem in src:
            if isinstance(elem,(dict)) == True:
                if not (elem.get(dest) is None):
                    return True
                values = elem.values()
                for value in values:
                    if Elements.contains(src=value,dest=dest) == True:
                        return True
            if isinstance(elem , (list,tuple)) == True:
                return Elements.contains(src = elem,dest = dest)
        return False

    """
	Description:
    	A recursive method that check the object `src` has the key `dest`.
	Paramater:
   		src: source object. It can be Any. However, the value of item will be checked iff it is one of these types: list,tuple,dict.
        dest: key that we want to find.
    Returned Value:
		Return True iff  `src` has the key `dest`.  Otherwise, return False.
	NOTICE: 
    	1. It may invoke the method itself. Thus, it may spend some time if the given `src` is too complicated.
    """     
    @staticmethod
    def contains_key(src,dest) -> bool:
        if dest == src :
            return True
        if isinstance(src,(list,tuple,dict)) == False:
            return False
        for elem in src:
            if isinstance(elem,(dict)) == True:
                keys = elem.keys()
                for key in keys:
                    if dest == key:
                        return True
                values = elem.values()
                for value in values:
                    if Elements.contains_key(src=value,dest=dest) == True:
                        return True
        return False
    
    """
	Description:
    	A recursive method that get the first corresponding value of key `dest` in the object `src`.
	Paramater:
   		src: source object. It can be Any. However, the value of item will be checked iff it is one of these types: list,tuple,dict.
        dest: key as target.
    Returned Value:
		Return the corresponding value of key `dest` iff `src` has the key `dest`. Otherwise, return the macro FOUNDMARCO.NOTFOUND.
	NOTICE: 
    	1. It may invoke the method itself. Thus, it may spend some time if the given `src` is too complicated.
        2. FOUNDMACRO which defined in found_macro file must be imported.
    """   
    @staticmethod
    def get_value_by_key(src,dest):
        if isinstance(src,(dict)) == True:
            keys = src.keys()
            for key in keys:
                if dest == key:
                    return src[key]
            result = Elements.get_value_by_key(src=src[key],dest=dest)
            if  result != FoundMacro.NOTFOUND:
                return result
        if isinstance(src,(list,tuple)) == True:
            for elem in src:
                result = Elements.get_value_by_key(src=elem,dest=dest)
                if  result != FoundMacro.NOTFOUND:
                    return result
        return FoundMacro.NOTFOUND
    
    """
	Description:
    	A recursive method that get all corresponding value of key `dest` in the object `src`.
	Paramater:
   		src: source object. It can be Any. However, the value of item will be checked iff it is one of these types: list,tuple,dict.
        top_dest: a key that should be on top level of `inner_dests`.
        inner_dests: keys as target.
    Returned Value:
		Return the corresponding value of key `inner_dests` iff `src` has the key `dest`. Otherwise, return an empty [[]].
	NOTICE: 
    	1. It may invoke the method itself. Thus, it may spend some time if the given `src` is too complicated.
        2. FOUNDMACRO which defined in found_macro file must be imported.
    """
    @staticmethod
    def get_all_values_by_key(src,top_dest,inner_dests : list ):
        results_2D = list()
        datas = Elements.get_value_by_key(src=src,dest=top_dest)
        for data in datas:
            results_1D = list()
            for inner_dest in inner_dests:
                result = Elements.get_value_by_key(src=data,dest=inner_dest)
                results_1D.append(result)
            results_2D.append(results_1D)
        return results_2D
    
    """
	Description:
    	A recursive method that get all corresponding value of key `dest` in the object `src`.
	Paramater:
   		src: source object. It can be Any. However, the value of item will be checked iff it is one of these types: list,tuple,dict.
        top_dest: a key that should be on top level of `inner_dests`.
        inner_dests: keys as target.
    Returned Value:
		Return the corresponding value of key `inner_dests` iff `src` has the key `dest`. Otherwise, return an empty [[]].
	NOTICE: 
    	1. It may invoke the method itself. Thus, it may spend some time if the given `src` is too complicated.
        2. FOUNDMACRO which defined in found_macro file must be imported.
    """
    @staticmethod
    def get_value_by_dict(src,mapping:dict)->dict:
        mapping_items = list(mapping.items())
        mapping_item_count = len(mapping_items)
        mapping_matched_count = 0
        mapping_top_level_key = FoundMacro.NOTFOUND
        mapping_top_level_value = FoundMacro.NOTFOUND

        if mapping is None:
            return ( FoundMacro.NOTFOUND,FoundMacro.NOTFOUND , FoundMacro.NOTFOUND , FoundMacro.NOTFOUND , FoundMacro.NOTFOUND)
        
        if isinstance(src,(list,tuple)) == True:
            for key_jth in range(0,len(src),1):
                elem = src[key_jth]
                if isinstance(elem,(dict)) == True:
                    keys = list(elem.keys())
                    mapping_matched_count = 0
                    for key_ith in range(0,len(keys),1):
                        key = keys[key_ith]
                        value = elem.get(key)
                        mapping_top_level_key = key
                        for mapping_item in mapping_items:
                            if isinstance(value,(dict)) == True:
                                result = Elements.get_value_by_dict(src=value,mapping=mapping)
                                mapping_top_level_value = value
                                return ( key_jth,key_ith , result[2] ,mapping_top_level_key, mapping_top_level_value)
                            elif isinstance(value,(list,tuple)) == True:
                                for key_kth in range(0,len(value),1):
                                    elem = value[key_kth]
                                    result = Elements.get_value_by_dict(src=value,mapping=mapping)
                                    mapping_top_level_value = value
                                    if result[0] != FoundMacro.NOTFOUND:
                                        return ( key_jth,key_kth , result[2] ,mapping_top_level_key, mapping_top_level_value)
                            elif key == mapping_item[0] and value == mapping_item[1]:
                                mapping_matched_count += 1  
                        if mapping_matched_count >= mapping_item_count:
                            return ( key_jth , key_ith,elem,mapping_top_level_key, mapping_top_level_value)
                        
                        
        elif isinstance(src,(dict)) == True:
            values = src.values()
            for key_jth in range(0,len(values),1):
                value = values[key_jth]
                result  = Elements.get_value_by_dict(src=value,mapping=mapping)
                mapping_top_level_value = value
                if result[0] != FoundMacro.NOTFOUND:
                    return ( 0 , key_jth , result[2] , mapping_top_level_key, mapping_top_level_value)
        return ( FoundMacro.NOTFOUND,FoundMacro.NOTFOUND,FoundMacro.NOTFOUND,FoundMacro.NOTFOUND,FoundMacro.NOTFOUND)
    
    """
	Description:
    	A recursive method that delete specified item `mapping` in the object `src`.
	Paramater:
   		src: source object. It can be Any. However, the value of item will be checked iff it is one of these types: list,tuple,dict.
        mapping: a dict
    Returned Value:
		Returns the result after deleting the specified item. 
	NOTICE: 
    	1. It may invoke the method itself. Thus, it may spend some time if the given `src` is too complicated.
    """
    @staticmethod
    def delete_specified_item(src,mapping):
        if isinstance(src,(dict)) == True:
            result = dict()
            for key,value in src.items():
                if isinstance(value,(dict,list,tuple)) == True:
                    result_temp = Elements.delete_specified_item(src=value,mapping=mapping)
                    result[key] = result_temp
                elif not(key in list(mapping.keys()) and value in list(mapping.values())):
                    result[key] = value           
            return result
        elif isinstance(src,(list,tuple)):
            result = list()
            for elem in src:
                if isinstance(elem,(dict,list,tuple)) == True:
                    result_temp = Elements.delete_specified_item(src=elem,mapping=mapping)
                    result.append(result_temp)
            return result
    @staticmethod
    def dict_to_list_2D(src:dict,projection:list):        
        results_2D = list()
        for find_result in src:
            result_1D = list()
            for proj in projection:
                if Elements.is_empty(src=find_result[proj]) == True:
                    raise ValueError('find_result[proj] can not be null or empty.')
                result_1D.append(find_result[proj])
            results_2D.append(result_1D)
        return results_2D
    
    """
	Description:
    	A recursive method that delete specified record `mapping` in the object `src`.
	Paramater:
   		src: source object. It can be Any. However, the value of item will be checked iff it is one of these types: list,tuple,dict.
        mapping: a dict
    Returned Value:
		Returns the result after deleting the specified record. 
	NOTICE: 
    	1. It may invoke the method itself. Thus, it may spend some time if the given `src` is too complicated.
    """
    @staticmethod
    def delete_specified_record(src:list|tuple|dict,mapping:dict,depth: int = 0 ,running_flag : bool= True):
        if isinstance(depth,(int)) != True:
            raise TypeError('depth must be a int.')
        if isinstance(mapping,(dict)) != True:
            raise TypeError('mapping must be a dict.')
        if isinstance(src,(list,tuple,dict)) != True:
            if depth == 0 :
                raise TypeError('src:list|tuple|dict.')
        if isinstance(running_flag,(bool)) != True:
            raise TypeError('running_flag must be a bool.')
    
        if isinstance(src,(dict)) == True:
            if src == mapping:
                return None
        
        if isinstance(src,(dict)) == True:
            temp_result_dict = dict()
            for elem_key,elem_value in src.items():
                if isinstance(elem_value,(list,tuple,dict)) != True:
                    if not ( elem_key in list(mapping.keys()) and elem_value in list(mapping.values()) ):
                        if running_flag == True:
                            temp_result_dict[elem_key] = elem_value
                    else:
                        running_flag = False
                elif isinstance(elem_value,(dict)) == True:
                   temp_result = Elements.delete_specified_record(src=elem_value,mapping=mapping,running_flag=running_flag)
                   if not Elements.is_empty(src=temp_result):
                       temp_result_dict[elem_key] = elem_value
            return temp_result_dict
        
        if isinstance(src,(list,tuple)) == True:
            temp_result_list = list()
            for elem in src:
                temp_result = Elements.delete_specified_record(src=elem,mapping=mapping,running_flag=True)
                if not Elements.is_empty(src=temp_result):
                    temp_result_list.append(temp_result)
            return temp_result_list


    """
	Description:
    	A recursive method that update its value whose item satisfies a dict `filter` to json_data` in the object `src`.
	Paramater:
   		src: source object. It can be Any. However, the value of item will be checked iff it is one of these types: list,tuple,dict.
        filter: a dict as filter
        json_data: a dict that will be updated to if needed.
        
    Returned Value:
		Returns the result after deleting the specified record. 
	NOTICE: 
    	1. It may invoke the method itself. Thus, it may spend some time if the given `src` is too complicated.
    """ 
    @staticmethod
    def update_value_by_dict(src : list|dict,filter : dict = None,json_data : dict = None):
        if isinstance(src,(list,dict)) == False:
            raise TypeError('src must be a list or dict')

        matched_result = Elements.get_value_by_dict(src=src,mapping=filter)
        ( key_ith , matched_json_data , mapping_top_level_key, mapping_top_level_value ) = matched_result
        if matched_result[0] == FoundMacro.NOTFOUND :
            raise ValueError('Should not find_one_check_exist the argument named filter\n such that the return value of the function call Elements.get_value_by_dict(src=src,mapping=filter) is FoundMacro.NOTFOUND.')
        
        if isinstance(src,(list)) == True:
            mapping_top_level_value[key_ith].update(json_data)
        elif isinstance(src,(dict)) == True:
            mapping_top_level_value.update(json_data)
        return ( src , matched_result )
        
if __name__ == '__main__':
    import pprint    
    from bson.objectid import ObjectId

    src =  {'accountname': 'accountname2',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username2'
                }

    
    filters  = [
        {'accountname': 'accountname2'},
    ]

    
    src =  {'accountname': 'accountname2',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username2'
                }
    
    filters  = [
        {'accountname': 'accountname1'},
    ]

    
    src =  {
        'data':{
                'accountname': 'accountname2',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username2'
                }
    }
        
    filters  = [
        {'accountname': 'accountname2'},
    ]

    
    src =  {
        'data':{
                'accountname': 'accountname2',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username2'
                },
        'tax':{
                'accountname': 'accountname1',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username1'
                }
    }
        
    filters  = [
        {'accountname': 'accountname2'},
    ]
    
    src =  [
                {'accountname': 'accountname2',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username2'
                },
                {
                'accountname': 'accountname1',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username1'
                }
    ]
        
    filters  = [
        {'accountname': 'accountname2'},
    ]
    
    
    src =  {
        'data':[
                {
                'accountname': 'accountname2',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username2'
                },
                {
                'accountname': 'accountname1',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username1'
                }
        ]
    }
        
    filters  = [
        {'accountname': 'accountname2'},
    ]
    
    '''
    src =  {
        'name': 'account_list',
        'data':[
                {
                'accountname': 'accountname2',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username2'
                },
                {
                'accountname': 'accountname1',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username1'
                }
        ]
    }
        
    filters  = [
        {'accountname': 'accountname2'},
    ]

    
    src =  [
        { 'name': 'account_list' },
        { 'data':[
                {
                'accountname': 'accountname2',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username2'
                },
                {
                'accountname': 'accountname1',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username1'
                }
        ]
        }
    ]
        
    filters  = [
        {'accountname': 'accountname2'},
    ]
    
    src =  [
                {'accountname': 'accountname2',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username2'
                },
                {
                    'accountname': 'accountname1',
                    'email_name': 'jayw711@gmail.com',
                    'password_name': 'password1',
                    'username': 'username1'
                },
                {'accountname': 'accountname3',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username3'
                },
        ]
        
    filters  = [
        {'accountname': 'accountname2'},
    ]
    

    
    src =  {'_id': ObjectId('665c0417bc07ebeeebaa69dc'),
        'data': [
                {'accountname': 'accountname2',
                'email_name': 'jayw@gmail.com',
                'password_name': '3er5t43ert4',
                'username': 'username2'
                },
                {
                    'accountname': 'accountname1',
                    'email_name': 'jayw711@gmail.com',
                    'password_name': 'password1',
                    'username': 'username1'
                },
        ],
        'database': 'tax',
        'name': 'account_list',
        'type': 'table'}    

    filters  = [
        {'accountname': 'accountname2'},
    ]
    '''

    pprint.pprint(src)
    print('-'*50)
    for ith in range(0,len(filters),1):
        filter = filters[ith]
        """
        Elements.init()
        Elements.delete_specified_record(src=src,mapping=filter)
        print('-'*25+str(ith)+'th'+'-'*25)
        pprint.pprint(filter)
        print('-'*50)
        pprint.pprint(Elements.static_result)
        print('-'*50)
        pprint.pprint(Elements.static_result_list)
        print('-'*50)
        print('~'*50)
        """
        result = Elements.delete_specified_record(src=src,mapping=filter)
        print('-'*25+str(ith)+'th'+'-'*25)
        pprint.pprint(filter)
        print('-'*50)
        pprint.pprint(result)
        print('-'*50)
        print('~'*50)
    print('!'*50)