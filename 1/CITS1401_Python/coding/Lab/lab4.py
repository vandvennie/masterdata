def list_sorting(lst1,lst2):
    dic={}
    for x in lst1:
        ind1=lst1.index(x)
        dic[x]=lst2[ind1]

    lstNA=list(dic.items())
    lstNA.sort(key=lambda x: (-x[1], x[0]))
    lstNA1=[item[0] for item in lstNA]
    lstNA2=[item[1] for item in lstNA]

    return lstNA1,lstNA2
print(list_sorting(['Chris','Amanda','Boris','Charlie'],[35,43,55,35]))
