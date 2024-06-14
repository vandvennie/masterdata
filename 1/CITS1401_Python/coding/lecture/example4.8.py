def emails():
    infile= input("enter the file name with students' detail: " )
    outfile=input("enter the file name where you want e,ail list ot be stored: ")

    #st_file=open(infile,'r')
    #em_file=open(infile,'w')
    email_date=''
    with open(infile,"r") as st_file:

        for line in st_file:
            sid,fname,lname = line.split(",")
            e_add=fname+'.'+lname[:-1]+'.'+sid+"@gmail.com\n"
            email_date=email_date+e_add

        #em_file.write(e_add.lower())

    #st_file.close()
    #em_file.close()
    with open(outfile,"w") as em_file:
        em_file.write(email_date)

    print("all the email address are written in the file ",outfile)

emails()