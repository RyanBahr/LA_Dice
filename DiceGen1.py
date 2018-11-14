from LA_Dice import DiceRoller

class Dice_Gen:

    def __init__(self, ndice):
        self.ndice = ndice
        masterlist = []
        currentlist = []

    def __iter__(self):
        return self

    def __next__(self):
        if (len(masterlist)) == ndice ** 2:
            raise StopIteration
            return masterlist
        else:
            self.current_roll = DiceRoller.combineLowestDiceOnce(self.current_roll)
            return self.current_roll
def main():
    r=Dice_Gen([1,1,1,1,1,1,1,1])
    for n in r:
        print(n)

if __name__ == "__main__":
    main()
