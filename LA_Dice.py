import random
class DiceRoller():
    def rollDice(number_of_dice):
        raw_results = []
        for y in range(0, number_of_dice):
            raw_results.append(random.randint(1,6))
        return raw_results
    def combineDice(raw_results):
        for x in
