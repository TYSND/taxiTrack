# Apriori.py by lpjworkroom
# naive apriori algorithm
#
# step:
#   1. get minimun support threshold
#   2. while item sets not empty:
#       count items support
#       remove items less than threshold

from itertools import combinations
from ItemSet import ItemSet,itemsetOccurence
from utils import log

debug=True

class Apriori():
    __minSup=0 # minimun support threshold
    __items=[] # store item sets
    __debug=True

    def __init__(self,minSup,items):
        # initiat items and item occurence,to be done...
        assert type(minSup) is int and (minSup>0),\
            "support threshold must be positive integer"
        self.__minSup=minSup
        self.initItems(items)

    def initItems(self,items):
        # count every itemset's occurence
        occurDict={}
        for itemset in items:
            tup=tuple(itemset)
            occurDict[tup]=(occurDict[tup]+1) if tup in occurDict else 1
        for tup,occur in occurDict.items():
            self.__items.append(ItemSet(list(tup),occur))
    
    def solve(self):
        remain=self.__items.copy()
        k=1 # k th item set
        while True:
            candi=self.getCandidateSets(remain,k) # get candidate item set list with length k from items
            log(debug,'candidates:',candi,'k=',k)
            freq=[] # frequent itemsets remained
            if len(candi)==0: # k bigger than elements count,no combination
                return remain
            for itemset in candi:
                log(debug,itemset,'occurs:',itemsetOccurence(itemset,self.__items))
                if itemsetOccurence(itemset,self.__items)>=self.__minSup:
                    freq.append(itemset)
            log(debug,'frequent itemsets:',freq,'k=',k)
            # no more frequent itemsets
            if len(freq)==0:
                return remain if k!=1 else []   # return last loop item sets if not at first loop
            remain=freq.copy()
            k+=1

    @staticmethod
    def getCandidateSets(items,lenth):
        # generate all combinations with lenth from elements in all itemsets
        ele=set()
        for itemset in items: # unify elements
            for element in itemset:
                ele.add(element)
        return [list(tup) for tup in combinations(list(ele),lenth)]

        
    
