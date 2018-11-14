import LA_Dice

class Dice_Generator:
    def __init__(self, raw_dice):
        self.current_roll = raw_dice

    def __next__(self):
        if (len(self.current_roll)) != len(set(self.current_roll)):
            yield self.current_roll
            raise StopIteration
        else:
            return self.current_roll
            self.current_roll = DiceRoller.combineLowestDiceOnce(self.current_roll)
def main():
    results = []
    r=Dice_Generator([1,1,1,1,1,1,1,1,1])
    for n in r:
        results.append(n)
    print(results)

if __name__ == "__main__":
    main()
