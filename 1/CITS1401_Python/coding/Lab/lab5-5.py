def make_dictionary(filename):
    with open(filename,'r') as file:
        file_date=file.read().split('\n')
    dic={}
    for a in file_date:
        if a:
            dic[a]=dic.get(a,0)+1
        
    return dic

dictionary = make_dictionary('data.txt')
for key in sorted(dictionary.keys()):
    print(key + ': ' + str(dictionary[key]))