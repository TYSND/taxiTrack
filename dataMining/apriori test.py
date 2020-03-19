from Apriori import Apriori
from getTransactionDB import getTransactionDB
from time import time


recordSum=[50,100,500,1000,5000,10000,50000]
#recordSum=[10000]
threshold=0.3

with open('output.txt','w') as output:
    for rec in recordSum:
        thre=int(rec*threshold)
        beg=time()
        a=Apriori(thre,getTransactionDB(rec).getTransactionList())
        out=a.solve()
        timeCost=time()-beg
        output.write('recordSum:%d threshold:%d MFI amount:%d MFI size:%d\n'%\
                     (rec,thre,len(out),len(out[0])))
        
