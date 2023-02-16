def sort_key1(val):
	return val[0]
def sort_key2(val):
	return val[1]

def IsBetweenLine(li:list)->bool:
    for idx in range(0,len(li),1):
        li_idx=li[idx]
        for jdx in range(idx+1,len(li),1):
            li_jdx=li[jdx]
            if (li_jdx[1]-li_idx[1])*(li_jdx[0]-li_idx[0])*(li_jdx[0]-li_idx[1])<0:
                print("They are ")
                print((li_jdx[1]-li_idx[1]))
                print((li_jdx[0]-li_idx[0]))
                print((li_jdx[0]-li_idx[1]))
                print("respectively.")
                return True,idx,jdx,li_idx,li_jdx
    return False,-1,-1,[],[]


def main():
    for cnt in range(0,10,1):
        list1=[[6+cnt, 19+3*cnt], [30, 46+cnt*cnt], [8, 18+2*cnt]]

        list1.sort(key=sort_key1, reverse=False)

        result,idx,jdx,li_idx,li_jdx=IsBetweenLine(list1)
    
        print("start of ------------------------------------------ no."+str(cnt))
    
        print(list1)
        print(result)
        print(idx)
        print(jdx)
        print(li_idx)
        print(li_jdx)

        print("end of ------------------------------------------ no."+str(cnt))

if __name__=='__main__':
    main()
