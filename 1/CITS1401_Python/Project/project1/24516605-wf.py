

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

            #Users whose age falls within the lower and upper bound of input age_group (inclusive)   
            if int(d_age) >= int(age_group[0]) and int(d_age) <= int(age_group[-1]):
            #OP2: A list of unique countries
                if d_country not in OP2s:
                    OP2s.append(d_country)
            #OP3
                #Hours spent by users
                hour_sum += float(d_hours)
                hour_list.append(d_hours)

                income_sum += float(d_income)
                income_list.append(d_income) 

                if d_area not in area_list:
                    area_list.append(d_area)

                age_sum += float(d_age)
                age_list.append(d_age)

                hour_area=[d_hours,d_area]
                hour_area_list.append(hour_area)
                    
            #Built a new list for OP4
            age_income_p=[d_age,d_income,d_platform]
            age_income_list.append(age_income_p)

            if d_platform not in platform_list:
                platform_list.append(d_platform)
    
        #OP3[0]: A numeric value for average time spent by users
        averag_hour=hour_sum/len(hour_list)

        #OP3[1]: A standard deviation of their income
        averag_income=income_sum/len(income_list)
        a=0
        for income_n in income_list:
            a += (float(income_n) - averag_income)**2

        standard=(a/(len(income_list)-1))**(1/2)

        #OP3[2]: a string for demography name that represents users falling within the age_group (inclusive) spent the lowest average time on social media
        hour_area_sum=0
        max_value=0
        max_area_list=[]
        for area_detail in area_list:
            len_area=0
            for hour_area_detail in hour_area_list:
                if hour_area_detail[-1] == area_detail:
                    hour_area_sum += float(hour_area_detail[0])
                    len_area += 1
                if len_area > 0:
                    averag_hour_area = hour_area_sum / len_area 
                else:
                    0#need to put some error 
            if averag_hour_area > max_value:
                max_value = averag_hour_area
                max_area_list.append(area_detail)
            elif averag_hour_area == max_value:
                max_area_list.append(area_detail)
        max_area=(sorted(max_area_list))[0]

        OP3s=[float("{:.4f}".format(averag_hour)),float("{:.4f}".format(standard)),max_area]


    #OP4: Correlation value
    b=0
    c=0
    d=0
    max_user=0
    max_p_list=[]
    #The social media platform that has the highest number of use
    for platform_detail in platform_list:
        e=0
        for xy in age_income_list:
            if xy[-1] == platform_detail:
                e += 1
        if e > max_user:
            max_user= e
            max_p_list.append(platform_detail)
        elif e > max_user:
            max_p_list.append(platform_detail)
        max_p=(sorted(max_p_list))[0]

    #average
    for xy in age_income_list:
        if xy[-1] == max_p:
            age_list4.append(xy[0])
            age_sum4 += float(xy[0])
        
            income_list4.append(xy[1]) 
            income_sum4 += float(xy[1])
            
    averag_age4 =float("{:.4f}".format(age_sum4/len(age_list4)))
    averag_income4 =float("{:.4f}".format(income_sum4/len(income_list4)))

#Correlation between age and income base of the social media platform
    for xy in age_income_list:
        if xy[-1] == max_p:
            b += ((float(xy[0]) - averag_age4)*(float(xy[1]) - averag_income4))
            c += (float(xy[0]) - averag_age4)**2
            d += (float(xy[1]) - averag_income4)**2
  
        if c*d != 0:
           correlation = b/((c*d)**(1/2))
        else:
           correlation = 0
    OP4s=float("{:.4f}".format(correlation))
    #OP4s=[averag_age4,averag_income4]

    return OP1s,sorted(OP2s),OP3s,OP4s
    
OP1,OP2,OP3,OP4=main('SocialMedia.csv', [18,25], 'australia')
print(OP1) 
print(OP2)
print(OP3)
print(OP4)    



