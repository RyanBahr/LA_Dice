import unittest
import LA_Dice
import math

class LivingAlchemyTest(unittest.TestCase):
    def test_equal_dice(self): #Tests that the number of rolled dice equals the
        self.assertEqual(10, len(LA_Dice.DiceRoller.rollDice(10)))
    def test_combine_dice(self): #tests whether dice combine correctly.
        testinglist = LA_Dice.DiceRoller.combineDice([1,1,2,2,3,3,4,4,5,5,6,6])
        self.assertEqual(len(testinglist), len(set(testinglist)))
    def test_highest_number(self): #tests to ensure that a role with N dice doesn't have a result which is higher than possible.
        testinglist1 = LA_Dice.DiceRoller.combineDice([1,1,2,2,3,3,4,4,5,5,6])
        self.assertFalse(max(testinglist1) > 6+math.log2(len(testinglist1)))

if __name__ == '__main__':
    unittest.main()
