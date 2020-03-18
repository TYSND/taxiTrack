# Apriori.py by lpjworkroom
# naive apriori algorithm
#
# step:
#   1. get minimun support threshold
#   2. while item sets not empty:
#       count items support
#       remove items less than threshold

from itertools import combinations


class ItemSet(list):
    occurence=0 # number of set's occurence

class Apriori:
    minSup=0 # minimun support threshold
    items=[] # store item sets

    def __init__(self):
        # initiat items and item occurence,to be done...
        pass
    
    def solve(self):
        items=self.items.copy()
        k=1 # k th item set
        while True:
            candi=self.getCandidateSets(items,k) # get candidate item set with length k from items
            if count(candi)==0: # k bigger than elements count,no combination
                return items
            freq=[] # frequent sets for next loop
            for itemset in candi:
                if self.itemsetOccurence(itemset,self.items)>=self.minSup:
                    freq.append(itemset)
            # no more frequent itemsets,return last loop item sets
            if count(freq)==0:
                return items
            items=freq
            k+=1

    def getCandidateSets(items,lenth):
        # generate all combinations with lenth from elements in all itemsets
        ele=set()
        for itemset in items: # unify elements
            for element in itemset:
                ele.add(element)
        return [combinations([ele],lenth)]

    def itemsetOccurence(target,records):
        for itemset in records:
            occur=True
            for ele in target: # check if all element in target occurs
                if itemset.count(ele)==0:
                    occur=False
                    break
            yield itemset.occurence if occur else 0
    
