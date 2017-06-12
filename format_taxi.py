import math

KEIDO0 = -122.4
IDO0 = 37.75
PIE=3.141592
R=6371000
R2=math.cos(math.radians(37.75))*R
for num in range(2):
    if num<10:
        filenum="00"+str(num)
    elif num<100:
        filenum="0"+str(num)
    else:
        filenum=str(num)
    fin=open("ID"+filenum+".txt")
    fout=open("newID"+filenum+".txt","w")
    data=fin.readlines()[::-1]
    for d in data:
        ido=float(d.split()[0])
        keido=float(d.split()[1])
        time=int(d.split()[3])

        x=2*PIE*R2*(keido-KEIDO0)/360
        y=2*PIE*R*(ido-IDO0)/360
        fout.writelines(str(x)+" "+str(y)+" "+str(time)+"\n")
    fin.close
    fout.close
