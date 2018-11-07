import random
class DiceRoller():
    def rollDice(number_of_dice):
        raw_results = []
        for y in range(0, number_of_dice):
            raw_results.append(random.randint(1,6))
        return raw_results
    def combineDice(raw_results):
        good_results = []
        for z in raw_results:
            if raw_results.count(z) == 1:
                good_results.append(z)
            elif raw_results.count(z) > 1:
                good_results.append(z+1)
                raw_results.remove(z)
        if len(good_results) != len(set(good_results)):
           return DiceRoller.combineDice(good_results)
        else:
            return good_results
