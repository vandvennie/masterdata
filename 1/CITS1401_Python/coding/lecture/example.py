def emails():
    infile= input("enter the file name with students' detail: " )
    outfile=input("enter the file name where you want e,ail list ot be stored: ")

    st_file=open(infile,'r')
    em_file=open(infile,'w')

    for line in st_file:
        sid,fname,lname = line.split(",")
        e_add=fname+'.'+lname[:-1]+'.'+sid+"@gmail.com\n"

        em_file.write(e_add.lower())

    st_file.close()
    em_file.close()

    print("all the email address are written in the file ",outfile)

emails()