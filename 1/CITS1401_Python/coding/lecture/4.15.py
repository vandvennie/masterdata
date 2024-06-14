def aveNum():
    count =0
    total=0
    num=input("enter a number: ")

    while num!="":
        num=float(num)
        count +=1
        total+=num
        num=input("enter a number: ")
        #moredate= input("more number?(y/n): ")
    print('average of ',count," number inserted is: ",total/count)

aveNum()

