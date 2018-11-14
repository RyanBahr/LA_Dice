import random
import math
from itertools import product

def checkduplicates(aList):
    if count(aList) == count(set(aList)):
        return True
    else:
        return False

class DiceRoller():
    def listMaker(raw_results): #makes a list of all first-level combinations given a set of dice
        all_results = []
        throwawaylist = []
        for x in set(raw_results):
            if raw_results.count(x) > 1:
                for z in raw_results:
                    if z != x:
                        throwawaylist.append(z)
                for a in range(1, (raw_results.count(x)-1)):
                    throwawaylist.append(x)
                throwawaylist.append(x+1)
            if throwawaylist != []:
                all_results.append(sorted(throwawaylist))
                throwawaylist = []
        return all_results

    def megaListMaker(raw_results):
        all_all_results = []
        fakelist = []
        for x in DiceRoller.listMaker(raw_results):
            all_all_results.append(x)
        for x in all_all_results:
            for y in DiceRoller.listMaker(x):
                all_all_results.append(y)
        for x in all_all_results:
            if x not in fakelist:
                fakelist.append(x)
        all_all_results = fakelist
        all_all_results.append(raw_results)
        return sorted(all_all_results)

Mylist = list(product(range(1,7), repeat=3))
MyRealList = []
for x in Mylist:
    MyRealList.append(list(x))
print(MyRealList)
#print(sorted(DiceRoller.listMaker([1,1,1,1,1,1,1,1])))
#print(DiceRoller.megaListMaker([1,1,2,2,3,3,4,4,]))
#print(DiceRoller.megaListMaker([1,1,1,1,1,1,1,1]))
#print(DiceRoller.SetMaker([[1,2,3],[4,5,6], [3,2,1], [6,5,4]]))
