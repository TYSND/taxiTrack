# ItemSet.py by lpjworkroom
# defines itemset used and often used methods in data mining

from utils import log

debug=False

def itemsetOccurence(target,records):
    # return occurence of target itemset in records list
    # contained by other itemset is counted too
    # like [1,2] in [1,2,3]
    ret=0
    for itemset in records:
        occur=True
        for ele in target: # check if all element in target occurs
            if itemset.count(ele)==0:
                occur=False
                break
        log(debug,target,'in',itemset,':',occur,'occurence:',itemset.occurence)
        ret+=itemset.occurence if occur else 0
    return ret


class ItemSet(list):
    occurence=0 # number of set's occurence
    def __init__(self,item,occur):
        super(ItemSet,self).__init__(item)
        self.occurence=occur
        
