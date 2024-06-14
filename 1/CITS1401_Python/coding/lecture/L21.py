#1.read the documents
#2.seperate words with spare and makes is case insensitive
#3.make a sets to store those words
#4.find how many times each word appears with a Loop 

def main():
    intro()
    txt = fileRead()
    ctext=textfilter(txt)
    dword=wcount(ctext)
    wordCount=list(dword.items())
    wordCount.sort(key=lambda x:x[1],reverse=True)
    #items(): Returns a sequence of tuples (key, value) representing the key-value pairs (i.e., 2-tuples).

    for item in wordCount:
        print(item)
    



def intro():
    print("this program counts the frequencies of the words in a file.")
    print("the uwser has to provide the mame of the file and put the file in the same folder. ")

def fileRead():
    fname=input("enter the name of the text file: ")

    try:
        with open(fname,"r") as fread:
            text=fread.read()
    except IOError:
        print("File cant be found or reached")
        return ""
    return text

def textfilter(text):
    text=text.lower()

    spCh="!@#$%^&*()_+{}|:<>?[]\;,.\"/~'1234567890"
    for sc in spCh:
        text =text.replace(sc," ")
    return text

print(textfilter("How r u ?:LG how"))

def wcount(text):
    wlist=text.split()
    wdict={}
    for word in wlist:
        wdict[word] = wdict.get(word,0) +1
        #get(): If dictionary has key, returns its value; otherwise returns default.
        return wdict