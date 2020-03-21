from Apriori import Apriori
from getTransactionDB import getTransactionDB
from time import time


#recordSum=[50,100,500,1000,5000,10000,50000]
recordSum=[5000]
threshold=0.15
rec=recordSum[0]
thre=int(rec*threshold)
beg=time()
a=Apriori(thre,getTransactionDB(rec).getTransactionList())
out=a.solve()
timeCost=time()-beg
data='recordSum:%d,threshold:%d,MFI amount:%d,MFI size:%d,time cost:%f secs\n'%\
        (rec,thre,len(out),len(out[0]),timeCost)
print(data)
print(out)
exit(0)


with open('output.txt','w') as output:
    for rec in recordSum:
        thre=int(rec*threshold)
        beg=time()
        a=Apriori(thre,getTransactionDB(rec).getTransactionList())
        out=a.solve()
        timeCost=time()-beg
        data='recordSum:%d,threshold:%d,MFI amount:%d,MFI size:%d,time cost:%f secs\n'%\
                     (rec,thre,len(out),len(out[0]),timeCost)
        print(data)
        output.write(data)
        
