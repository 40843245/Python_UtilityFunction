# Intro to utility class
## In FindValuesWithKeyInNestedDict.py

### Intro to its method
Given a nested data (for any common type (such as tuple,list,dict)), one can 

1. search specific data in nested data (i.e. one or more values contains either list,tuple,set,dict) Such as o={'1':'a','2':'b',['3','4',{'5':'f'}]}

In the method GetValueByKeyInNestedDatas(self,data,key,containValue:bool) of the class Data,

The parameters and usage as follows.
    
    1) data: The origin data that we will search for. 
    
    2) key: The target as keyword to search for.
    
    3) containValue: It can be set to boolean value. It determines the values will be searched.
    
      When it is set to False, only the key will be searched.
      
      That is, it will search for the keys of all dictsm, additionally, it will search values in list, tuple, and sets those contain nested type recursively.
      
      If the key is found in the original data, then the corresponding values will be returned.
      
      NOTE that if the value is found in original data, it will be ignored and it continues to search.
      
      If the key is NOT found in the original data, it will return self.NOTFOUND which is defined to -1.
      
      When it is set to True, all the keys and values will be searched.
      
      That is, it will search for the keys of all dicts, additionally, it will search values in list, tuple, and sets those contain nested type recursively.
      
      NOTE that if the value is found in original data, it will be returned.

In the method GetNestedData(self,data) of the class Data,

The parameters and usage as follows.

    This method will expand a nested data named data into a single list then store it into self.result.
    
    It is a utility method for the method GetNestedDatas(self,data).
    
    1) data : The origin data that we will search for. 
    
In the method GetNestedDatas(self,data) of the class Data,

    This method will perform GetNestedData(self,data) then return self.result.
    
    1) data : The origin data that we will search for. 
    
    
### Example 
Example 1
    
        o={'1':'a','2':'b','3':['4','5',{'6':'f'}]}
    
  The expected output of GetNestedDatas(data=o) should be
  
    ['1', 'a', '2', 'b', '3', ['4', '5', {'6': 'f'}]]
    
