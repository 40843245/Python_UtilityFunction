result=[]
def Print_NestedData(data):
      global result
      if data is None:
          return None     
      if isinstance(data,(str,int,bool)):
          result.append(data)
          return None
      if isinstance(data,(tuple,set,list)):
          for v in data:
              Print_NestedData(v)
          return None
      if isinstance(data,(dict)):
          for k,v in data.items():
              if len(k)==1:
                  result.append(k)
              else:
                  Print_NestedData(k)          
              if len(v)==1:
                  result.append(v)       
              else:
                  Print_NestedData(v)
          return None

# Driver code to test data.
o={'1':'a','2':'b','3':['4','5',{'6':'f'}]}
Print_NestedData(data=o)
print("result=")
print(result)
