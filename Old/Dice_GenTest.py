import LA_Dice

class Dice_Generator:
    def __init__(self, raw_dice, max):
        self.current_roll = raw_dice
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        yield self.current_roll
        if (len(self.current_roll)) > self.max:
            raise StopIteration
        else:
            self.current_roll.append(1)
def main():
    results = []
    r=Dice_Generator([1,1,1,1,1,1,1,1,1])
    for n in r:
        results.append(n)
    print(results)

if __name__ == "__main__":
    main()
