import LA_Dice

class Dice_Generator:
    def __init__(self, raw_dice):
        self.raw_dice = raw_dice
        results = []

    def __iter__(self):
        self.current_roll = raw_dice
        return self

    def __next__(self):
        self.results.append(self.current_roll)
        if (len(self.current_roll)) != len(set(self.current_roll)):
                self.current_roll = LA_Dice.DiceRoller.combineLowestDiceOnce(current_roll)
        else:
            return results
            raise StopIteration
