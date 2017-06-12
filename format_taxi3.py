DAYLEN=86400    #=60*60*24
id=0            #file id
for num in range(2):
    if num<10:
        filenum="00"+str(num)
    elif num<100:
        filenum="0"+str(num)
    else:
        filenum=str(num)
    fin=open("secondID"+filenum+".txt")
    tmp=fin.readlines()
    filelen=len(tmp)
    st=int(tmp[0].split()[2])
    et=int(tmp[filelen-1].split()[2])
    st2=st-st%DAYLEN+DAYLEN
    et2=et-et%DAYLEN
    fin.seek(0)
    for d in range((DAYLEN-st%DAYLEN)):
        fin.readline()
    while st2<et2 :
        id +=1
        st2+=DAYLEN
        fout=open("formatedID"+str(id)+".txt","w")
        for t in range(DAYLEN):
            x=fin.readline()
            fout.writelines(str(t)+" "+x)
        fout.close()
    fin.close()
