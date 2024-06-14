def bsearch(x,lst):
    start = 0
    end = len(lst) -1
    while start<=end:# make a loop
        mid=(start+end)//2
        item=lst[mid]
        if x == item:
            return mid
        elif x>item:
            start=mid+1
        else:
            end=mid-1
    return None