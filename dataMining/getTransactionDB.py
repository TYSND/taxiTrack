import random
class getTransactionDB:
	__items=[]
	__src=""
	__transNum=0
	
	def __init__(self,src,transNum):
		self.__src=src
		self.__transNum=transNum
	def __init__(self,transNum):
		self.__transNum=transNum
	def getItems(self):
		#...
		#...
		#...
		for i in range(0,21):
			self.__items.insert(i,i)
	def getTransactionList(self):
		transList=[]
		self.getItems()
		i=0
		l=len(self.__items)#项目集合的大小
		#print(l)
		ceil=2**l
		#print(ceil)
		
		while i<self.__transNum:
			tmplst=[]
			lstnum=random.randint(1,ceil-1)
			cnt=0
			while cnt<=l:
				tmp=lstnum&(1<<cnt)
				if tmp>0:
					tmplst.append(self.__items[cnt])
				#print(cnt)
				cnt+=1
			transList.append(tmplst)
			i+=1
		print(transList)
		return transList
		

if __name__ == "__main__":
	gtdb=getTransactionDB(10)
	gtdb.getTransactionList()
		
