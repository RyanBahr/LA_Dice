class Primenumber(object):
    def __init__(self, end): # Init instead of __iter__ here
        self._end = end

    def checkprimenumber(self,n):
        for i in range(2,n):
            if n%i==0:
                return False
        return True

    def __iter__(self):
        yield 2
        if self._end>2:
            for n in range(2,self._end):
                if self.checkprimenumber(n): # Need to call to self.
                    yield n
def main():
    r=Primenumber(150)
    for n in r:
        print(n)

if __name__ == "__main__":
    main()
