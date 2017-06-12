import math

for num in range(2):
    if num<10:
        filenum="00"+str(num)
    elif num<100:
        filenum="0"+str(num)
    else:
        filenum=str(num)
    fin=open("newID"+filenum+".txt")
    fout=open("secondID"+filenum+".txt","w")
    data=fin.readlines()
    for i in range(1,len(data)):
        t1=int(data[i].split()[2])
        t0=int(data[i-1].split()[2])
        x1=float(data[i].split()[0])
        x0=float(data[i-1].split()[0])
        y1=float(data[i].split()[1])
        y0=float(data[i-1].split()[1])
        dt=(t1-t0)
        dx=(x1-x0)/dt
        dy=(y1-y0)/dt
        for j in range(0,dt):
            fout.writelines(str(x0+j*dx)+" "+str(y0+j*dy)+" "+str(t0+j)+"\n")
    fout.writelines(data[len(data)-1])
    fin.close
    fout.close
