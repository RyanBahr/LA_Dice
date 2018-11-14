class Primenumber(object):
    def __init__(self, current_roll): # Init instead of __iter__ here
        self.current_roll = current_roll

    def checknoduplicates(self,current_roll):
        if (len(self.current_roll)) == len(set(self.current_roll)):
            return True
        else:
            return False

    def combineLowestDiceOnce(self,current_roll):
        self.good_results = []
        for z in set(self.current_roll):
            if self.current_roll.count(z) > 1 and z == min(self.current_roll):
                for x in range(0,(self.current_roll.count(z)-2)):
                    self.current_roll.append(z)
                self.good_results.append(z+1)
            else:
                for x in range(self.current_roll.count(z)):
                    self.good_results.append(z)
            return self.good_results

    def __iter__(self):
        if self.checknoduplicates(self.current_roll): # Need to call to self.
            yield self.current_roll
        else:
            self.current_roll = self.combineLowestDiceOnce(self.current_roll)
def main():
    r=Primenumber([1,1,1,1])
    for n in r:
        print(n)

if __name__ == "__main__":
    main()
