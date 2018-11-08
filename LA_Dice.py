import random
import math

def hasDuplicates

class DiceRoller():
    def rollDice(number_of_dice):
        raw_results = []
        for y in range(0, number_of_dice):
            raw_results.append(random.randint(1,6))
        return raw_results

    def combineDice(raw_results):
        good_results = []
        for z in set(raw_results):
            if raw_results.count(z) == 1:
                good_results.append(z)
            elif raw_results.count(z) > 1 and raw_results.count(z) % 2 == 0:
                for x in range(0,(raw_results.count(z)//2)):
                    good_results.append(z+1)
            elif raw_results.count(z) > 1 and raw_results.count(z) % 2 != 0:
                for x in range(0,((raw_results.count(z)-1)//2)):
                    good_results.append(z+1)
                good_results.append(z)
        if len(good_results) != len(set(good_results)):
           return DiceRoller.combineDice(good_results)
        else:
#            return good_results
            return "Good Results are %s, Raw Results are %s" % (good_results, raw_results)
            #print(DiceRoller.combineDice([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]))

    def combineLowestDiceOnce(raw_results):
        good_results = []
        for z in set(raw_results):
            if raw_results.count(z) > 1 and z == min(raw_results):
                for x in range(0,(raw_results.count(z)-2)):
                    good_results.append(z)
                good_results.append(z+1)
            else:
                for x in range(raw_results.count(z)):
                    good_results.append(z)
#            return good_results
        return "Good Results are %s, Raw Results are %s" % (good_results, raw_results)

class Dice_Generator:
    def __init__(self, raw_dice):
        self.current_roll = raw_dice
        self.results = []

    def __next__(self):
        self.results.append(self.current_roll)
        if (len(self.current_roll)) != len(set(self.current_roll)):
                self.current_roll = LA_Dice.DiceRoller.combineLowestDiceOnce(current_roll)
        else:
            return results
            raise StopIteration
