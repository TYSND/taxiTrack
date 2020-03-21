from Apriori import Apriori
from getTransactionDB import getTransactionDB
from time import time


threshold=0.15
rec=5000
thre=int(rec*threshold)
beg=time()
a=Apriori(thre,getTransactionDB(rec).getTransactionList())
out=a.solve()
timeCost=time()-beg
data='recordSum:%d,threshold:%d,MFI amount:%d,MFI size:%d,time cost:%f secs\n'%\
        (rec,thre,len(out),len(out[0]),timeCost)
print(data)
print(out)
