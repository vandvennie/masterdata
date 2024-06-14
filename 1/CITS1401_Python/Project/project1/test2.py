

def main(csvfile, age_group, country):
    # open an argument csvfile
    with open(csvfile, 'r') as file:
        #find indexes of header in the file, and handle in case-insensitiv of header
        head=file.readline().lower()
        cell_head=head.strip().split(",")
        index_ID=cell_head.index('id')
        index_age=cell_head.index('age')
        index_hours=cell_head.index("time_spent_hour")
        index_platform=cell_head.index("platform")
        index_country=cell_head.index("country")
        index_area=cell_head.index("demographics")
        index_income=cell_head.index('income')
        index_indebt=cell_head.index("indebt")
        

        OP1s=[]
        OP2s=[]
        OP3s=[]
        OP4s=[]
        hour_sum=0
        hour_list=[]
        income_sum=0
        income_list=[]
        income_sum4=0
        income_list4=[]
        area_list=[]
        age_sum=0
        age_list=[]
        age_sum4=0
        age_list4=[]
        platform_list=[]
        hour_area_list=[]
        age_income_list=[]

        
        


        #find value of every cell to prepare for comparing if it match comditions. All string data in the file is case-insensitive
        for line in file:
            line=line.lower().strip().split(",")
            d_id = line[index_ID]
            d_age = line[index_age]
            d_hours = line[index_hours]
            d_platform=line[index_platform]
            d_country = line[index_country]
            d_area = line[index_area]
            d_income = line[index_income]
            d_indebt = line[index_indebt]

            #OP1:A list containing list(s) of student details [ID and income]from the country provided as input who are in debt and spends more than 7 hours on any social media
            if d_country == country.lower() and d_indebt == "true" and d_hours > "7":
                OP1=[d_id ,float("{:.2f}".format(float(d_income)))]
                OP1s.append(OP1)

        def creat_list(index_x):
            xsum=0
            xlist=[] 
            for line in file:
                line=line.lower().strip().split(",")
                d_x=line[index_x]
                xsum += float(d_x)
                xlist.append(d_x)
            return xsum,xlist
            #Users whose age falls within the lower and upper bound of input age_group (inclusive)  
             
        if int(d_age) >= int(age_group[0]) and int(d_age) <= int(age_group[-1]):
            #OP2: A list of unique countries
                if d_country not in OP2s:
                    OP2s.append(d_country)
            #OP3
                #Hours spent by users
                hour_sum,hour_list=creat_list(index_hours)
                #hour_sum += float(d_hours)
                #hour_list.append(d_hours)

                income_sum,income_list=creat_list(index_income)
                #income_sum += float(d_income)
                #income_list.append(d_income) 

                
    return OP1s,OP2s,hour_list,income_list
    
OP1,OP2,OP3,OP4=main('SocialMedia.csv', [18,25], 'australia')
print(OP1) 
print(OP2)
print(OP3)
print(OP4)    



