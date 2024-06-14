def files(csvfile):
    with open(csvfile, "r") as file:
        lines = file.readlines()  # Read all lines from the file
        
        # Process header
        head = lines[0].lower().strip().split(',')
        
        # Process data rows
        data_list = []
        for line in lines[1:]:
            data = line.lower().strip().split(',')
            data_list.append(data)
    
    dic_data = {}
    #dic_data['id'] = ['age', 'time_spent_hour', 'engagement_score', 'profession', 'platform', 'income']
    index_id = head.index("id")
    index_age = head.index("age")
    index_tsh = head.index("time_spent_hour")
    index_es = head.index("engagement_score")
    index_platform = head.index("platform")
    index_profession = head.index("profession")
    index_income = head.index("income")
    
    for data in data_list:
        if (data[index_id] and data[index_age] and data[index_tsh] and data[index_es] and
            data[index_profession] and data[index_platform] and data[index_income]
        ):
            dic_data[data[index_id]] = [
            data[index_age], data[index_tsh], data[index_es],
            data[index_platform], data[index_profession], data[index_income]
            ]
    
    return dic_data
#print (files('social_media.csv'))

#dic_data['id'] = ['age', 'time_spent_hour', 'engagement_score', 'profession', 'platform', 'income']
# data-cleaning 
    # clean duplicated data
    # clean missing or invalid data
        # data cannot be null
        # age cannot be negative,
        # user ids must be alphanumeric
        # engagement score cannot be non-numeric
        # time_spent_hour cannot be non-numeric
        # income cannot be non-numeric
def is_numeric(s):
    for char in s:
        if not char.isdigit() and char != '.':
            return False
    return True
#has_space_between_alphabets
def has_or_not_space(s):
    # Iterate through the characters in the string
    for i in range(len(s) - 1):
        # Check if the current character is a space
        if s[i] == ' ':
            # Check if the adjacent characters are alphabetic
            if s[i - 1].isalpha() and s[i + 1].isalpha():
                return True
    return False

def clean(filedata):
    cleaned_data={}
    dic_data=files(filedata)

    for key,value in dic_data.items():
        if key.isalnum():
            if (float(value[0])>0 and float(value[1])>0 and
                is_numeric(value[2]) and value[3].isalpha() and 
                has_or_not_space(value[4]) and value[5].isdigit()
                ):
                cleaned_data[key]=[
                value[0],value[1],value[2],value[3],value[4],value[5]
                ]
    return cleaned_data

print(clean('social_media.csv'))



        