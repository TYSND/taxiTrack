from Apriori import Apriori
from getTransactionDB import getTransactionDB
a=Apriori(5,getTransactionDB(10).getTransactionList())
print('solve:',a.solve())
