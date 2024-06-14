# This program is Project2 for course 1401, submitted by student Zhulin LYU (24516605) at the UWA
# The aim of this project is to analyse the data to better understand social media usage and its impact.


def files(csvfile):
    """
    Build a function to read a file
    This function will handle case insensitivity
    It will also clean missing data and extract useful data to insert into a dictionary
    Param: file name
    Output: data dictionary
    """
    with open(csvfile, "r") as file:
        lines = file.readlines()  # Read all lines from the file
        
        # Process header
        head = lines[0].lower().strip().split(',')
        
        # Process data rows
        data_list = []
        for line in lines[1:]:
            data = line.lower().strip().split(',')
            data_list.append(data)
    # Keep the necessary columns in a dictionary
    dic_data = {}
    index_id = head.index("id")
    index_age = head.index("age")
    index_tsh = head.index("time_spent_hour")
    index_es = head.index("engagement_score")
    index_platform = head.index("platform")
    index_profession = head.index("profession")
    index_income = head.index("income")
    # Ignore the empty data and delete lines with the same ID
    for data in data_list:
        if (data[index_id] and data[index_age] and data[index_tsh] and data[index_es] and
            data[index_profession] and data[index_platform] and data[index_income]
        ):
            if data[index_id] in dic_data:
                del dic_data[data[index_id]]
            else:
                # dic_data['id'] = ['age', 'time_spent_hour', 'engagement_score', 'platform', 'profession', 'income']
                # index:              0             1                  2               3            4           5
                dic_data[data[index_id]] = [
                data[index_age], data[index_tsh], data[index_es],
                data[index_platform], data[index_profession], data[index_income]
                ]
    
    return dic_data

def is_numeric(s):
    """
    Build a function to estimate if it is a float
    Param: any data
    Output: True or False
    """
    try:
        float(s)  # Try to convert the string to a float
        return True  
    except ValueError:
        return False  
    

def has_or_not_space(s):
    """
    Build a function to determine if it is an alphanumeric data even with spaces
    Param: any data
    Output: True or False
    """
    return all(char.isalpha() or char.isspace() for char in s)


def clean(filedata):
    """
    Build a function to clean:
    1.Clean missing or invalid data
    2.Data cannot be null
    3.Age cannot be negative,
    4.User ids must be alphanumeric
    5.Engagement score cannot be non-numeric
    6.Time_spent_hour cannot be non-numeric
    7.Income cannot be non-numeric
    Param: file 
    Output the dictionary in the following format
    cleaned_data['id'] = ['age', 'time_spent_hour', 'engagement_score', 'platform', 'profession', 'income']
    index:                 0             1                  2               3            4           5
    """
    cleaned_data={}
    dic_data=files(filedata)

    for key,value in dic_data.items():
        if key.isalnum():
            try:
                if(float(value[0])>=0 and float(value[1])>=0 and is_numeric(value[2]) 
                    and has_or_not_space(value[4]) and value[5].isdigit()
                    ):
                        cleaned_data[key]=[
                        value[0],value[1],value[2],value[3],value[4],value[5]
                        ]
            except ValueError:
                continue
    return cleaned_data


def ave(nlist):
    """
    Build a function to calculate the average
    Param: a list
    Output: a number
    """
    ave=sum(nlist)/len(nlist)
    return ave

def standardd(nlist):
    """
    Build a function to calculate the standard deviation
    Param: a list
    Output: a number
    """
    average=ave(nlist)
    numerator=sum((float(num)-average)**2 for num in nlist)
    sd=(numerator/(len(nlist)-1))**(1/2)
    return sd
    
def engaget(tsh,es):
    """
    Build a function to calculate the Engagement time
    Engagement time = (time_spent_hour x engagement_score) / 100
    Param: time_spent_hour and engagement_score
    Output: a number
    """
    et=(float(tsh)*float(es))/100
    return et

def cosine(listab,lista,listb):
    """
    Build a function to calculate the Cosine
    Param: three lists
    Output: a number
    """
    sum=0
    for x in listab:
        sum+=float(x[0])*float(x[1])

    sesum_a=0
    se_a=0
    for x in lista:
        sesum_a+=float(x)**2
    se_a=sesum_a**(1/2)

    sesum_b=0
    se_b=0
    for x in listb:
        sesum_b+=float(x)**2
    se_b=sesum_b**(1/2)

    cos=sum/(se_a*se_b)
    return cos
    

def pools(list1,list2):
    """
    Build a function to calculate the pooled standard deviation
    Param: two lists
    Output: a number
    """
    s1=standardd(list1)
    s2=standardd(list2)
    n1=len(list1)
    n2=len(list2)
    up=(n1-1)*(s1**2)+(n2-1)*(s2**2)
    s=(up/(n1+n2-2))**(1/2)
    return s

def cohen(list1,list2):
    """
    Build a function to calculate the Cohen’s d test
    Param: two lists
    Output: a number
    """
    d= (ave(list1)-ave(list2))/pools(list1,list2)
    return d

def op1(filedata):
    """
    Build a function to calculate OP1
    Items is ID of the user and value is a list containing age, time_spent_hour, and engagement_score
    Param: file
    Output: a dictionary
    """

    dic1={}
    dic2={}
    list1=[]
    list2=[]
    list_op1=[]
    data_dict=clean(filedata)

    for key,value in data_dict.items():
        if value[4]=='student':
            list1=[int(value[0]),int(value[1]),float(value[2])]
            dic1[key]=list1
            
        else:
            list2=[int(value[0]),int(value[1]),float(value[2])]
            dic2[key]=list2
    list_op1=(dic1,dic2)  
         
    return list_op1

def op2(filedata):
    """
    Build a function to calculate OP2
    A dictionary where key is a platform and value is a list
    Param: file
    Output: a dictionary of the total, average and standard deviation of engagement time of users using that platform.
    """
    dic={}
    dvalue=[]
    dic_et={}
    et_values=[]
    data_dict=clean(filedata)

    for key,value in data_dict.items():
        et = engaget(value[1], value[2])
        if value[3] in dic_et:
            et_values = dic_et[value[3]]
            et_values.append(et)
        else:
            et_values = [et]
            
        dic_et[value[3]] = et_values

    # Calculate statistics for each platform
    for platform, datalist in dic_et.items():
        try:
            total_value = round(sum(datalist),4)
            ave_value = round(ave(datalist),4)     
            sd_value = round(standardd(datalist),4)
            dvalue = [total_value,ave_value,sd_value]
            dic[platform] = dvalue
        except ZeroDivisionError:
            dic[platform] = []
    return dic

# Build a function to calculate OP3
# A list of two numeric values calculating the cosine similarity between the age and income 
# for users whose profession is “student” and for the users whose profession is not student
def op3(filedata):
    """
    Build a function to calculate OP3
    A list of two numeric values calculating the cosine similarity between the age and income 
    Param: a file
    Output: a list
    """
    lis=[]
    slista=[]
    slisti=[]
    slistai=[]
    nslista=[]
    nslisti=[]
    nslistai=[]
    data_dict=clean(filedata)

    for key,value in data_dict.items():
        if value[4]=='student':
            slista.append(value[0])
            slisti.append(value[5])
            sai=[value[0],value[5]]
            slistai.append(sai)
        else:
            nslista.append(value[0])
            nslisti.append(value[5])
            nsai=[value[0],value[5]]
            nslistai.append(nsai)

    #Cosine
    try:
        scos=round(cosine(slistai,slista,slisti),4)
        nscos=round(cosine(nslistai,nslista,nslisti),4)
        lis=[scos,nscos]
        return lis

    except ZeroDivisionError:
        # Error: Standard Deviation Division by zero!s
        lis=[]  # Returning None to indicate an error
        return lis

def op4(filedata):
    """
    Build a function to calculate OP4
    A numeric value for Cohen’s d test for engagement time to find the difference between two groups
    Param: a file
    Output: a number
    """
    slist=[]
    nslist=[]
    data_dict=clean(filedata)

    for key,value in data_dict.items():
        et=engaget(value[1],value[2])
        if value[4]=='student':
            slist.append(et)
        else:
            nslist.append(et)

    try:
        ct=round(cohen(slist,nslist),4)
        return ct
    except ZeroDivisionError:
        # Error: Standard Deviation Division by zero!
        ct = 0 # Returning None to indicate an error
        return ct

# A main function of the project
def main(csvfile):
    try:
        op1_value,op2_value,op3_value,op4_value=op1(csvfile),op2(csvfile),op3(csvfile),op4(csvfile)
        return op1_value,op2_value,op3_value,op4_value
    except FileNotFoundError:    
        print("Invalid input. No such file or directory:", csvfile)




OP1, OP2, OP3, OP4 = main('insensitive.csv')
print(len(OP1[0]))
print(len(OP1[1]))
