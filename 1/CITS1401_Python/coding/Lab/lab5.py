def make_index(words_on_page):
    li=words_on_page.items()
    dic={}
    for a in li:
        for b in a[1]:
            b=b.split(',')
            for c in b:
                if c not in dic:
                    dic[c] = [a[0]]
                    
                else:
                    dic[c].append(a[0])
    return dic

input_dict = {
   1: ['hi', 'there', 'fred'], 
   2: ['there', 'we', 'go'],
   3: ['fred', 'was', 'there']}
#print (make_index(input_dict))
output_dict = make_index(input_dict)
for word in sorted(output_dict.keys()):
    print(word + ': ' + str(output_dict[word]))

#fred: [1, 3]
#go: [2]
#hi: [1]
#there: [1, 2, 3]
#was: [3]
#we: [2]