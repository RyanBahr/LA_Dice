from LA_Dice import DiceRoller

class Dice_Gen:

    def __init__(self, current_roll):
        self.current_roll = current_roll

    def __iter__(self):
        return self

    def __next__(self):
        if (len(self.current_roll)) == len(set(self.current_roll)):
            raise StopIteration
            return self.current_roll
        else:
            self.current_roll = DiceRoller.combineLowestDiceOnce(self.current_roll)
            return self.current_roll
def main():
    r=Dice_Gen([1,1,1,1,1,1,1,1])
    for n in r:
        print(n)

if __name__ == "__main__":
    main()
