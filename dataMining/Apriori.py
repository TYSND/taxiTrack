# Apriori.py by lpjworkroom
# naive sample of apriori algorithm
# step:
#   1 get minimun support threshold
#   2 while item sets not empty:
#       count items support
#       remove items less than threshold

class ItemSet(list):
    occurence=0 # number of set's occurence

class Apriori:
    minSup=0 # minimun support threshold
    items=[] # store item sets
    
    def solve(self):
        items=list(self.items)
        k=1 # k th item set
        while True:
            # get candidate item set with length k from items
            candi=self.getCandidateSets(items,k)
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
        # generate all itemsets of lenth from elements in all items' sets
        ele=set()
        for itemset in items:
            for element in itemset:
                ele.add(element)
        return combination(list(ele),)

    def itemsetOccurence(target,records):
        for itemset in records:
            occur=True
            for ele in target:
                if itemset.count(ele)==0:
                    occur=False
                    break
            yield itemset.occurence if occur else 0
    
