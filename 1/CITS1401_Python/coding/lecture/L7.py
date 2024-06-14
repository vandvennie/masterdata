def aveNum():
    count =0
    total=0
    num=input("enter multiple numbers separated by comma: ")

    while True:
        num=input("enter multiple numbers separated by comma: ")
        if num =="":
            break
        for item in num.split(','):
            #num=float(num)
            count +=1
            total+=float(item)
        #num=input("enter multiple number separated by comma: ")
        #moredate= input("more number?(y/n): ")
    print('average of ',count," number inserted is: ",total/count)

aveNum()

