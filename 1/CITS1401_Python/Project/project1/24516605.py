#This project is to analyse user demographics to better understand social media usage.
#This program is Program 1 for course 1401, submitted by student 24516605 at the UWA.

#Built main function of this project
def main(csvfile, age_group, country):
    #Open a file
    with open(csvfile, 'r') as file:
        #Find indexes of header in the file, and handle in case-insensitiv of header
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
        
        #Create some necessary argument
        OP1s=[]
        OP2s=[]
        OP3s=[]
        OP4s=[]
        income_list=[]
        area_list=[]
        platform_list=[]
        hour_income_area=[]
        age_income_list=[]
        age_income_list4=[]

        #A function of buiting a list and find an average of it
        def ave_list(temlist,index_x):
            xsum=0
            xlist=[] 
            averag = 0 
            index_x = int(index_x)
            for line in temlist:
                if index_x < len(line):
                    d_x=line[index_x]
                    xsum += float(d_x)
                    xlist.append(d_x)
                    if len(xlist)!=0:
                        averag=xsum/len(xlist)
            return xlist,averag
        
                    
        
        #A function of buiting a distinct values list
        def dist(d_x,distinctl):
            if d_x not in distinctl:
                distinctl.append(d_x)
            return distinctl

        #Find value of specified indexs from cells. All string data in the file is case-insensitive
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

            #OP1: A list containing list(s) of student details [ID and income]from the country provided as input who are in debt and spends more than 7 hours on any social media
            if d_country == country.lower() and d_indebt == "true" and d_hours > "7":
                OP1=[d_id ,float("{:.2f}".format(float(d_income)))]
                OP1s.append(OP1)

            #Users whose age falls within the lower and upper bound of input age_group (inclusive)  
            if int(d_age) >= int(age_group[0]) and int(d_age) <= int(age_group[-1]):

                #OP2: A list of unique countries
                OP2s=dist(d_country,OP2s)

                #OP3: Create a list which has matching age_group
                hour_income_area.append([d_hours,d_income,d_area,d_age,d_platform])

                #A list of unique demographics
                area_list=dist(d_area,area_list)
                    
            #Built two new lists for OP4
            age_income_list.append([d_age,d_income,d_platform])

            platform_list=dist(d_platform,platform_list)

            
        #OP3[0]: A numeric value for average time spent by users
        hour_list,averag_hour=ave_list(hour_income_area,0)
        
        #OP3[1]: A standard deviation of their income
        income_list,averag_income=ave_list(hour_income_area,1)
        a=0
        for income_n in income_list:
            a += (float(income_n) - averag_income)**2
        if (len(income_list)-1)!=0:
            standard=(a/(len(income_list)-1))**(1/2)
        else:
            standard=None

        #OP3[2]: a string for demography name that represents users falling within the age_group (inclusive) spent the lowest average time on social media
        hour_area_sum=0
        averag_hour_area=0
        max_value=0
        max_area_list=[]
        for area_detail in area_list:
            len_area=0
            for hour_area_detail in hour_income_area:
                if hour_area_detail[-1] == area_detail:
                    hour_area_sum += float(hour_area_detail[0])
                    len_area += 1
                if len_area > 0:
                    averag_hour_area = hour_area_sum / len_area 
                else:
                    OP3s=None
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

    #The average of age and income
    for xy in age_income_list:
        if xy[-1] == max_p:
            age_income_list4.append([xy[0],xy[1]])
    
    list4,averag_age4 = ave_list(age_income_list4,0)
    averag_age4 =float("{:.4f}".format(averag_age4))
    
    list4,averag_income4 = ave_list(age_income_list4,1)
    averag_income4 =float("{:.4f}".format(averag_income4))

#Correlation between age and income base of the social media platform
    for xy in age_income_list:
        if xy[-1] == max_p:
            b += ((float(xy[0]) - averag_age4)*(float(xy[1]) - averag_income4))
            c += (float(xy[0]) - averag_age4)**2
            d += (float(xy[1]) - averag_income4)**2
  
        if c*d != 0:
           correlation = b/((c*d)**(1/2))
        else:
           correlation = None
    OP4s=float("{:.4f}".format(correlation))

    return OP1s,sorted(OP2s),OP3s,OP4s
